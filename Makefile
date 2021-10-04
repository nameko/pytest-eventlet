static:
	pre-commit run --all-files

test:
	pytest tests.py -v

coverage:
	coverage run -m pytest tests.py -v
	coverage report
