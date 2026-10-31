from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files


def on_files(files: Files, config: MkDocsConfig) -> Files:
    root = Path(__file__).resolve().parent
    for directory in ("ejercicio-arquitectura-polizas", "self-test-app"):
        for source in sorted((root / directory).iterdir()):
            if not source.is_file() or source.suffix not in {".md", ".puml", ".py", ".yml"}:
                continue
            uri = source.relative_to(root).as_posix()
            existing = files.get_file_from_path(uri)
            if existing is not None:
                files.remove(existing)
            files.append(
                File(
                    uri,
                    src_dir=str(root),
                    dest_dir=config.site_dir,
                    use_directory_urls=config.use_directory_urls,
                )
            )
    return files
