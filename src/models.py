import uuid
from typing import List, Literal
from pydantic import BaseModel, Field, model_validator


class MinimalSource(BaseModel):
    """A single source location: a character span inside a corpus file."""

    file_path: str
    first_character_index: int = Field(ge=0)
    last_character_index: int = Field(ge=0)


class Chunk(MinimalSource):
    """Internal model: a piece of a corpus file stored in the index."""

    type: Literal["doc", "code"]
    text: str

    @model_validator(mode="after")
    def check_position(self) -> "Chunk":
        """To check that first index is smaller than last one"""
        diff = self.last_character_index - self.first_character_index
        if diff <= 0:
            raise ValueError(
                f"[ERROR]: {self.file_path} is incorrect, "
                "final index is smaller than starting one"
                )
        return self


class UnansweredQuestion(BaseModel):
    """A question that has not been answered yet."""

    question_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question: str


class AnsweredQuestion(UnansweredQuestion):
    """A question with its reference sources and answer."""

    sources: List[MinimalSource]
    answer: str


class RagDataset(BaseModel):
    """A dataset of RAG questions, answered or not."""

    rag_questions: List[AnsweredQuestion | UnansweredQuestion]


class MinimalSearchResults(BaseModel):
    """Search results for a single question."""

    question_id: str
    question: str
    retrieved_sources: List[MinimalSource]


class MinimalAnswer(MinimalSearchResults):
    """Search results for a single question, plus the generated answer."""

    answer: str


class StudentSearchResults(BaseModel):
    """Output of the ``search_dataset`` command."""

    search_results: List[MinimalSearchResults]
    k: int


class StudentSearchResultsAndAnswer(BaseModel):
    """Output of the ``answer_dataset`` command."""

    search_results: List[MinimalAnswer]
    k: int
