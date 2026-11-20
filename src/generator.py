class Generator():
    """Generate an answer from a question and its retrieved context"""

    def load_model(self) -> None:
        """Load the Qwen model or a specific one"""
        ...

    def build_prompt(self) -> None:
        """Build the prompt from the question and the context"""
        ...

    def generate_answer(self) -> None:
        """Generate the answer with the model"""
        ...

    def format_output(self) -> None:
        """Format the answer for the JSON output"""
        ...
