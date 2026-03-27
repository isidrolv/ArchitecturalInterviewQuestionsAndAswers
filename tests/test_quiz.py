"""
Unit tests for src/quiz.py.

Run with:
    pytest tests/test_quiz.py -v
"""

import pytest

from src.quiz import (
    Question,
    Quiz,
    ARCHITECTURAL_QUESTIONS,
    create_default_quiz,
)


# ===========================================================================
# Question tests
# ===========================================================================


class TestQuestionCreation:
    """Tests for the Question constructor."""

    def test_creates_question_with_required_fields(self):
        q = Question("What is REST?", "Representational State Transfer")
        assert q.question == "What is REST?"
        assert q.answer == "Representational State Transfer"
        assert q.options is None

    def test_creates_question_with_options(self):
        options = ["A", "B", "C", "D"]
        q = Question("Q?", "B", options=options)
        assert q.options == options

    def test_raises_on_empty_question_text(self):
        with pytest.raises(ValueError, match="question text cannot be empty"):
            Question("", "some answer")

    def test_raises_on_blank_question_text(self):
        with pytest.raises(ValueError, match="question text cannot be empty"):
            Question("   ", "some answer")

    def test_raises_on_empty_answer_text(self):
        with pytest.raises(ValueError, match="answer text cannot be empty"):
            Question("Some question?", "")

    def test_raises_on_blank_answer_text(self):
        with pytest.raises(ValueError, match="answer text cannot be empty"):
            Question("Some question?", "   ")

    def test_raises_when_answer_not_in_options(self):
        with pytest.raises(ValueError, match="answer must be one of the provided options"):
            Question("Q?", "E", options=["A", "B", "C", "D"])

    def test_raises_when_options_list_is_empty(self):
        with pytest.raises(ValueError, match="options list cannot be empty"):
            Question("Q?", "A", options=[])


class TestQuestionIsCorrect:
    """Tests for Question.is_correct()."""

    def setup_method(self):
        self.q = Question("What is REST?", "Representational State Transfer")

    def test_exact_match_returns_true(self):
        assert self.q.is_correct("Representational State Transfer") is True

    def test_case_insensitive_match_returns_true(self):
        assert self.q.is_correct("representational state transfer") is True
        assert self.q.is_correct("REPRESENTATIONAL STATE TRANSFER") is True
        assert self.q.is_correct("Representational state Transfer") is True

    def test_leading_trailing_whitespace_ignored(self):
        assert self.q.is_correct("  Representational State Transfer  ") is True

    def test_wrong_answer_returns_false(self):
        assert self.q.is_correct("Wrong answer") is False

    def test_empty_string_returns_false(self):
        assert self.q.is_correct("") is False

    def test_none_returns_false(self):
        assert self.q.is_correct(None) is False

    def test_partial_answer_returns_false(self):
        assert self.q.is_correct("Representational") is False

    def test_multiple_choice_correct_option(self):
        q = Question("Q?", "B", options=["A", "B", "C", "D"])
        assert q.is_correct("B") is True
        assert q.is_correct("b") is True

    def test_multiple_choice_wrong_option(self):
        q = Question("Q?", "B", options=["A", "B", "C", "D"])
        assert q.is_correct("A") is False
        assert q.is_correct("C") is False


# ===========================================================================
# Quiz tests
# ===========================================================================


class TestQuizCreation:
    """Tests for the Quiz constructor."""

    def test_creates_empty_quiz(self):
        quiz = Quiz()
        assert quiz.total_questions() == 0

    def test_creates_quiz_with_initial_questions(self):
        questions = [
            Question("Q1", "A1"),
            Question("Q2", "A2"),
        ]
        quiz = Quiz(questions=questions)
        assert quiz.total_questions() == 2

    def test_initial_score_is_zero(self):
        quiz = Quiz()
        assert quiz.score == 0

    def test_initial_answers_given_is_zero(self):
        quiz = Quiz()
        assert quiz.answers_given == 0

    def test_does_not_mutate_original_list(self):
        """The quiz must own a copy of the questions list."""
        original = [Question("Q1", "A1")]
        quiz = Quiz(questions=original)
        original.append(Question("Q2", "A2"))
        assert quiz.total_questions() == 1


class TestQuizAddQuestion:
    """Tests for Quiz.add_question()."""

    def test_add_question_increases_total(self):
        quiz = Quiz()
        quiz.add_question(Question("Q1", "A1"))
        assert quiz.total_questions() == 1

    def test_add_multiple_questions(self):
        quiz = Quiz()
        for i in range(5):
            quiz.add_question(Question(f"Q{i}", f"A{i}"))
        assert quiz.total_questions() == 5

    def test_raises_when_adding_non_question(self):
        quiz = Quiz()
        with pytest.raises(TypeError, match="must be an instance of Question"):
            quiz.add_question("not a question")  # type: ignore[arg-type]


class TestQuizGetQuestion:
    """Tests for Quiz.get_question()."""

    def setup_method(self):
        self.quiz = Quiz([Question("Q0", "A0"), Question("Q1", "A1")])

    def test_returns_correct_question_by_index(self):
        q = self.quiz.get_question(0)
        assert q.question == "Q0"

    def test_returns_last_question(self):
        q = self.quiz.get_question(1)
        assert q.question == "Q1"

    def test_raises_on_negative_index(self):
        with pytest.raises(IndexError):
            self.quiz.get_question(-1)

    def test_raises_on_index_equal_to_length(self):
        with pytest.raises(IndexError):
            self.quiz.get_question(2)

    def test_raises_on_index_far_out_of_range(self):
        with pytest.raises(IndexError):
            self.quiz.get_question(100)


class TestQuizGetRandomQuestion:
    """Tests for Quiz.get_random_question()."""

    def test_returns_a_question_instance(self):
        quiz = Quiz([Question("Q1", "A1"), Question("Q2", "A2")])
        q = quiz.get_random_question()
        assert isinstance(q, Question)

    def test_returned_question_belongs_to_quiz(self):
        questions = [Question(f"Q{i}", f"A{i}") for i in range(10)]
        quiz = Quiz(questions)
        q = quiz.get_random_question()
        assert q in quiz._questions

    def test_raises_on_empty_quiz(self):
        quiz = Quiz()
        with pytest.raises(ValueError, match="no questions"):
            quiz.get_random_question()


class TestQuizAnswerQuestion:
    """Tests for Quiz.answer_question()."""

    def setup_method(self):
        self.quiz = Quiz([Question("Q0", "A0"), Question("Q1", "A1")])

    def test_correct_answer_returns_true(self):
        result = self.quiz.answer_question(0, "A0")
        assert result is True

    def test_correct_answer_increments_score(self):
        self.quiz.answer_question(0, "A0")
        assert self.quiz.score == 1

    def test_wrong_answer_returns_false(self):
        result = self.quiz.answer_question(0, "wrong")
        assert result is False

    def test_wrong_answer_does_not_increment_score(self):
        self.quiz.answer_question(0, "wrong")
        assert self.quiz.score == 0

    def test_answers_given_increments_for_correct_answer(self):
        self.quiz.answer_question(0, "A0")
        assert self.quiz.answers_given == 1

    def test_answers_given_increments_for_wrong_answer(self):
        self.quiz.answer_question(0, "wrong")
        assert self.quiz.answers_given == 1

    def test_multiple_answers_tracked_correctly(self):
        self.quiz.answer_question(0, "A0")   # correct
        self.quiz.answer_question(1, "wrong")  # wrong
        assert self.quiz.score == 1
        assert self.quiz.answers_given == 2

    def test_raises_on_invalid_index(self):
        with pytest.raises(IndexError):
            self.quiz.answer_question(99, "A0")


class TestQuizGetPercentage:
    """Tests for Quiz.get_percentage()."""

    def test_returns_zero_when_no_answers_given(self):
        quiz = Quiz([Question("Q0", "A0")])
        assert quiz.get_percentage() == 0.0

    def test_returns_100_when_all_correct(self):
        quiz = Quiz([Question("Q0", "A0"), Question("Q1", "A1")])
        quiz.answer_question(0, "A0")
        quiz.answer_question(1, "A1")
        assert quiz.get_percentage() == 100.0

    def test_returns_50_when_half_correct(self):
        quiz = Quiz([Question("Q0", "A0"), Question("Q1", "A1")])
        quiz.answer_question(0, "A0")    # correct
        quiz.answer_question(1, "wrong")  # wrong
        assert quiz.get_percentage() == 50.0

    def test_returns_0_when_all_wrong(self):
        quiz = Quiz([Question("Q0", "A0")])
        quiz.answer_question(0, "wrong")
        assert quiz.get_percentage() == 0.0

    def test_percentage_based_on_answers_given_not_total(self):
        """Score % is based on answered questions, not quiz size."""
        quiz = Quiz([Question(f"Q{i}", f"A{i}") for i in range(10)])
        quiz.answer_question(0, "A0")  # 1 correct out of 1 answered
        assert quiz.get_percentage() == 100.0


class TestQuizReset:
    """Tests for Quiz.reset()."""

    def test_reset_clears_score(self):
        quiz = Quiz([Question("Q0", "A0")])
        quiz.answer_question(0, "A0")
        quiz.reset()
        assert quiz.score == 0

    def test_reset_clears_answers_given(self):
        quiz = Quiz([Question("Q0", "A0")])
        quiz.answer_question(0, "A0")
        quiz.reset()
        assert quiz.answers_given == 0

    def test_reset_does_not_remove_questions(self):
        questions = [Question("Q0", "A0"), Question("Q1", "A1")]
        quiz = Quiz(questions)
        quiz.reset()
        assert quiz.total_questions() == 2

    def test_can_answer_after_reset(self):
        quiz = Quiz([Question("Q0", "A0")])
        quiz.answer_question(0, "A0")
        quiz.reset()
        result = quiz.answer_question(0, "A0")
        assert result is True
        assert quiz.score == 1


# ===========================================================================
# Pre-loaded questions & factory function
# ===========================================================================


class TestArchitecturalQuestions:
    """Tests for the ARCHITECTURAL_QUESTIONS bank."""

    def test_bank_is_not_empty(self):
        assert len(ARCHITECTURAL_QUESTIONS) > 0

    def test_all_items_are_question_instances(self):
        for q in ARCHITECTURAL_QUESTIONS:
            assert isinstance(q, Question)

    def test_all_questions_have_non_empty_text(self):
        for q in ARCHITECTURAL_QUESTIONS:
            assert q.question.strip()

    def test_all_questions_have_non_empty_answer(self):
        for q in ARCHITECTURAL_QUESTIONS:
            assert q.answer.strip()

    def test_questions_with_options_have_valid_answer(self):
        for q in ARCHITECTURAL_QUESTIONS:
            if q.options is not None:
                assert q.answer in q.options


class TestCreateDefaultQuiz:
    """Tests for the create_default_quiz() factory."""

    def test_returns_quiz_instance(self):
        quiz = create_default_quiz()
        assert isinstance(quiz, Quiz)

    def test_quiz_contains_all_architectural_questions(self):
        quiz = create_default_quiz()
        assert quiz.total_questions() == len(ARCHITECTURAL_QUESTIONS)

    def test_factory_returns_independent_quizzes(self):
        """Modifying one quiz must not affect another."""
        quiz1 = create_default_quiz()
        quiz2 = create_default_quiz()
        quiz1.add_question(Question("Extra Q", "Extra A"))
        assert quiz1.total_questions() != quiz2.total_questions()

    def test_quiz_starts_with_zero_score(self):
        quiz = create_default_quiz()
        assert quiz.score == 0
