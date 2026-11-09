#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = $PSScriptRoot
$DocsRoot = Join-Path $Root "docs"
$Utf8 = [System.Text.UTF8Encoding]::new($false)
$Extensions = @(".md", ".pdf", ".txt", ".docx", ".html", ".puml", ".wsd")
$Files = @(Get-ChildItem -LiteralPath $DocsRoot -Recurse -File |
    Where-Object { $_.Extension -in $Extensions } |
    Sort-Object FullName)

function ConvertTo-LinkPath([string]$Path) {
    return (($Path -split '[\\/]' | ForEach-Object {
        [Uri]::EscapeDataString($_)
    }) -join '/')
}

function ConvertTo-YamlString([string]$Value) {
    return "'" + $Value.Replace("'", "''") + "'"
}

function Set-GeneratedBlock(
    [string]$Path,
    [string]$Start,
    [string]$End,
    [string[]]$Lines
) {
    $Content = [System.IO.File]::ReadAllText($Path)
    $Pattern = '(?s)' + [regex]::Escape($Start) + '.*?' + [regex]::Escape($End)
    if ([regex]::Matches($Content, $Pattern).Count -ne 1) {
        throw "Expected exactly one generated block in $Path"
    }
    $Newline = if ($Content.Contains("`r`n")) { "`r`n" } else { "`n" }
    $Block = (@($Start) + $Lines + @($End)) -join $Newline
    $Updated = [regex]::Replace(
        $Content, $Pattern, [System.Text.RegularExpressions.MatchEvaluator]{
            param($Match)
            $Block
        }
    )
    [System.IO.File]::WriteAllText($Path, $Updated, $Utf8)
}

$Toc = [System.Collections.Generic.List[string]]::new()
$Nav = [System.Collections.Generic.List[string]]::new()
$Nav.Add("nav:")
$Nav.Add("  - Inicio: index.md")
$Groups = $Files | Group-Object {
    $_.DirectoryName.Substring($DocsRoot.Length).TrimStart('\', '/')
} | Sort-Object Name

foreach ($Group in $Groups) {
    $Label = if ($Group.Name) { $Group.Name.Replace('\', ' / ') } else { "Inicio" }
    $Toc.Add("")
    $Toc.Add("### $Label")
    $Toc.Add("")
    $Pages = @($Group.Group | Where-Object {
        $_.Extension -eq ".md" -and $_.FullName -ne (Join-Path $DocsRoot "index.md")
    })
    if ($Pages.Count -gt 0) {
        $Nav.Add("  - $(ConvertTo-YamlString $Label):")
        foreach ($Page in $Pages) {
            $Relative = $Page.FullName.Substring($DocsRoot.Length + 1).Replace('\', '/')
            $Nav.Add("      - $(ConvertTo-YamlString $Page.BaseName): $(ConvertTo-YamlString $Relative)")
        }
    }
    foreach ($File in $Group.Group) {
        $Relative = $File.FullName.Substring($Root.Length + 1)
        $Title = if ($File.Extension -eq ".md") { $File.BaseName } else { $File.Name }
        $Title = $Title.Replace('[', '\[').Replace(']', '\]')
        $Toc.Add("- [$Title]($(ConvertTo-LinkPath $Relative))")
    }
}
$Toc.Add("")

Set-GeneratedBlock -Path (Join-Path $Root "README.md") `
    -Start "<!-- BEGIN 2026 TOC -->" -End "<!-- END 2026 TOC -->" -Lines $Toc.ToArray()
Set-GeneratedBlock -Path (Join-Path $Root "mkdocs.yml") `
    -Start "# BEGIN GENERATED NAV" -End "# END GENERATED NAV" -Lines $Nav.ToArray()

Write-Host "Indexed $($Files.Count) documents. Updated README.md and mkdocs.yml."
