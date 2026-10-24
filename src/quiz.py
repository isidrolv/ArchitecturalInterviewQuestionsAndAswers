"""
Architectural Interview Quiz Program.

Provides a Question / Quiz model and a bank of pre-loaded
architectural interview questions.
"""

from __future__ import annotations

import random
from typing import List, Optional


class Question:
    """Represents a single interview question with its expected answer.

    Parameters
    ----------
    question:
        The question text shown to the user.
    answer:
        The canonical correct answer (case-insensitive comparison is used).
    options:
        Optional list of multiple-choice options.  When provided the answer
        must be one of the option strings.
    """

    def __init__(
        self,
        question: str,
        answer: str,
        options: Optional[List[str]] = None,
    ) -> None:
        if not question or not question.strip():
            raise ValueError("question text cannot be empty")
        if not answer or not answer.strip():
            raise ValueError("answer text cannot be empty")
        if options is not None:
            if not options:
                raise ValueError("options list cannot be empty")
            if answer not in options:
                raise ValueError("answer must be one of the provided options")

        self.question: str = question
        self.answer: str = answer
        self.options: Optional[List[str]] = options

    def is_correct(self, user_answer: str) -> bool:
        """Return True if *user_answer* matches the correct answer (case-insensitive)."""
        if user_answer is None:
            return False
        return user_answer.strip().lower() == self.answer.strip().lower()

    def __repr__(self) -> str:  # pragma: no cover
        return f"Question(question={self.question!r}, answer={self.answer!r})"


class Quiz:
    """Manages a collection of :class:`Question` objects and tracks the score.

    Parameters
    ----------
    questions:
        Initial list of :class:`Question` objects.  Defaults to an empty list.
    """

    def __init__(self, questions: Optional[List[Question]] = None) -> None:
        self._questions: List[Question] = list(questions) if questions else []
        self._score: int = 0
        self._answers_given: int = 0

    # ------------------------------------------------------------------
    # Question management
    # ------------------------------------------------------------------

    def add_question(self, question: Question) -> None:
        """Append *question* to the quiz."""
        if not isinstance(question, Question):
            raise TypeError("question must be an instance of Question")
        self._questions.append(question)

    def get_question(self, index: int) -> Question:
        """Return the question at position *index*.

        Raises
        ------
        IndexError
            If *index* is out of range.
        """
        if index < 0 or index >= len(self._questions):
            raise IndexError(
                f"index {index} is out of range for quiz with "
                f"{len(self._questions)} question(s)"
            )
        return self._questions[index]

    def get_random_question(self) -> Question:
        """Return a random question from the quiz.

        Raises
        ------
        ValueError
            If the quiz has no questions.
        """
        if not self._questions:
            raise ValueError("quiz has no questions")
        return random.choice(self._questions)

    def total_questions(self) -> int:
        """Return the total number of questions in the quiz."""
        return len(self._questions)

    # ------------------------------------------------------------------
    # Answering & scoring
    # ------------------------------------------------------------------

    def answer_question(self, index: int, user_answer: str) -> bool:
        """Evaluate *user_answer* for the question at *index*.

        Increments the score when the answer is correct.

        Returns
        -------
        bool
            ``True`` if *user_answer* is correct, ``False`` otherwise.

        Raises
        ------
        IndexError
            If *index* is out of range.
        """
        question = self.get_question(index)
        self._answers_given += 1
        correct = question.is_correct(user_answer)
        if correct:
            self._score += 1
        return correct

    @property
    def score(self) -> int:
        """Current number of correct answers."""
        return self._score

    @property
    def answers_given(self) -> int:
        """Total number of answers submitted so far."""
        return self._answers_given

    def get_percentage(self) -> float:
        """Return the current score as a percentage (0–100).

        Returns ``0.0`` when no answers have been submitted.
        """
        if self._answers_given == 0:
            return 0.0
        return (self._score / self._answers_given) * 100.0

    def reset(self) -> None:
        """Reset the score and answer counter without removing questions."""
        self._score = 0
        self._answers_given = 0

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"Quiz(total_questions={self.total_questions()}, "
            f"score={self._score}, answers_given={self._answers_given})"
        )


# ---------------------------------------------------------------------------
# Pre-loaded architectural interview questions
# ---------------------------------------------------------------------------

ARCHITECTURAL_QUESTIONS: List[Question] = [
    Question(
        question="What is microservices architecture?",
        answer=(
            "An architectural style that structures an application as a "
            "collection of small, autonomous services"
        ),
    ),
    Question(
        question="What does SOLID stand for in software design?",
        answer=(
            "Single Responsibility, Open/Closed, Liskov Substitution, "
            "Interface Segregation, Dependency Inversion"
        ),
    ),
    Question(
        question="What is the CAP theorem?",
        answer=(
            "A distributed system cannot simultaneously guarantee Consistency, "
            "Availability, and Partition tolerance"
        ),
    ),
    Question(
        question="What is the difference between REST and SOAP?",
        answer=(
            "REST is a lightweight architectural style using HTTP; SOAP is a "
            "protocol with strict standards and XML messaging"
        ),
    ),
    Question(
        question="What is Event-Driven Architecture?",
        answer=(
            "An architectural pattern where components communicate through "
            "events, promoting loose coupling and scalability"
        ),
    ),
    Question(
        question="What is the DRY principle?",
        answer=(
            "Don't Repeat Yourself — every piece of knowledge should have a "
            "single, authoritative representation in the system"
        ),
    ),
    Question(
        question="What is Domain-Driven Design (DDD)?",
        answer=(
            "An approach that models software to match a domain, using a "
            "ubiquitous language shared by developers and domain experts"
        ),
    ),
    Question(
        question="What is CQRS?",
        answer=(
            "Command Query Responsibility Segregation — separating read and "
            "write operations into different models"
        ),
    ),
    Question(
        question=(
            "Which architectural pattern best describes a layered application "
            "with Presentation, Business Logic, and Data Access layers?"
        ),
        answer="N-Tier / Layered Architecture",
        options=[
            "Microservices Architecture",
            "Event-Driven Architecture",
            "N-Tier / Layered Architecture",
            "Serverless Architecture",
        ],
    ),
    Question(
        question="What is the Strangler Fig pattern?",
        answer=(
            "A migration strategy where new functionality is implemented in a "
            "new system while gradually replacing the legacy system"
        ),
    ),
]


def create_default_quiz() -> Quiz:
    """Return a :class:`Quiz` pre-loaded with all architectural questions."""
    return Quiz(questions=list(ARCHITECTURAL_QUESTIONS))
