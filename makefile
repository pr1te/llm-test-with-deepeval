# Run deepeval test on a specified file

venv:
	poertry shell

test:
	@if [ -z "$(file)" ]; then \
		echo "Usage: make test file=<file_path>"; \
		exit 1; \
	else \
		deepeval test run $(file); \
	fi
