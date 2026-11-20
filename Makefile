
.PHONY: install run debug clean clean_all lint lint-strict

install:
	uv sync

run:
	uv run python -m src

debug:
	uv run python -m src

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache

fclean: clean
	rm -rf .venv

lint:
	uv run flake8 .
	uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run flake8 .
	uv run mypy . --strict
