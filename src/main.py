from src.models import RagDataset


def main() -> None:
    """Entry point of the program"""
    with open("data/raw/vllm-0.10.1/vllm/model_executor/layers/fused_moe/fused_batched_moe.py", encoding="utf-8") as f:
        content = f.read()

    print(content[28416:28975])