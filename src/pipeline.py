from .indexer import Indexer
from .retriever import Retriever
from .generator import Generator


class Pipeline():
    """Orchestrate the indexer, the retriever and the generator"""

    def __init__(self) -> None:
        """Create the components used by the pipeline"""
        self.indexer = Indexer()
        self.retriever = Retriever()
        self.generator = Generator()

    def run_indexing(self) -> None:
        """Load the files, chunk them, build and save the index"""
        ...

    def run_search(self) -> None:
        """Search the top k sources for a single question"""
        ...

    def run_answer(self) -> None:
        """Search the sources and generate an answer for a single question"""
        ...

    def run_search_dataset(self) -> None:
        """Search the top k sources for every question of a dataset"""
        ...

    def run_answer_dataset(self) -> None:
        """Search and generate an answer for every question of a dataset"""
        ...
