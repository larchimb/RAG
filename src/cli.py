class Cli():
    """The class to handle all the CLI commands (one method = one command)"""

    def index(self, max_chunk_size: int = 2000) -> None:
        """Ingest data/raw/ and build the index under data/processed/"""
        print(f"[STUB] index: max_chunk_size={max_chunk_size}")

    def search(self, query: str, k: int = 10) -> None:
        """Return the top-k sources for a single query"""
        print(f"[STUB] search: query={query!r}, k={k}")

    def search_dataset(
        self, dataset_path: str, save_directory: str, k: int = 10
    ) -> None:
        """Run search over a dataset and save a StudentSearchResults JSON"""
        print(
            f"[STUB] search_dataset: dataset_path={dataset_path!r}, "
            f"k={k}, save_directory={save_directory!r}"
        )

    def answer(self, query: str, k: int = 10) -> None:
        """Answer a single query using the retrieved context"""
        print(f"[STUB] answer: query={query!r}, k={k}")

    def answer_dataset(
        self, student_search_results_path: str, save_directory: str
    ) -> None:
        """Generate answers for a dataset and save them as JSON"""
        print(
            "[STUB] answer_dataset: student_search_results_path="
            f"{student_search_results_path!r}, "
            f"save_directory={save_directory!r}"
        )

    def evaluate(
        self, student_search_results_path: str, dataset_path: str
    ) -> None:
        """Report recall@k of search results against a ground-truth dataset"""
        print(
            "[STUB] evaluate: student_search_results_path="
            f"{student_search_results_path!r}, "
            f"dataset_path={dataset_path!r}"
        )
