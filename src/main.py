from src.models import RagDataset, AnsweredQuestion, UnansweredQuestion, uuid, MinimalSource


def main() -> None:
    """Entry point of the program"""
    source = MinimalSource(file_path="data/datasets/AnseweredQuestions/dataset_code_public.json", first_character_index=0, last_character_index=2000)
    print(source)
