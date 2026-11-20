class Indexer():
    """Create the index for .py or .md files"""

    def load_files(self) -> None:
        """Find the files and check that they are readable"""
        ...

    def chunk_python(self) -> None:
        """Split a Python file into chunks by function"""
        ...

    def chunk_text(self) -> None:
        """Split a Markdown or text file into chunks"""
        ...

    def build_index(self) -> None:
        """Build the index with the BM25 method"""
        ...

    def save_index(self) -> None:
        """Save the index to the right path"""
