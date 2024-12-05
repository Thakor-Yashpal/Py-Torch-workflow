train:
	python scripts/train.py

test:
	pytest

lint:
	flake8 tests/ src/

clean:
	rm -rf __pycache__ .pytest_cache

all: lint test train  # Define a default target