import fire

from .cli import Cli

try:
    fire.Fire(Cli)
except KeyboardInterrupt:
    print("[ERROR]: Keyboard interruption from the user")
except Exception as e:
    print(f"[ERROR]: {e}")
