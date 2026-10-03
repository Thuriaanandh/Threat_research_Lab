.PHONY: help test lint validate clean

help:
	@echo "Threat Research Lab Automation Makefile"
	@echo "----------------------------------------"
	@echo "make test       : Run full pytest test suite"
	@echo "make validate   : Run repository and detection rule validation"
	@echo "make clean      : Clean temporary cache files"

test:
	pytest tests/ -v

validate:
	python scripts/utilities/validate_repo.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
