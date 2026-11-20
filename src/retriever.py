class Retriever():
    """Find the top k result in the index"""

    def load_index(self) -> None:
        """Load the index saved by the indexer"""
        ...

    def search(self) -> None:
        """Find the chunks matching the query"""
        ...

    def rank_results(self) -> None:
        """Rank the results of the search"""
        ...

    def get_top_k(self, k: int) -> None:
        """Get the first k results"""
        ...
