black:
	black src/*.py tests/*.py

coverage:
	pytest --cov=src tests/

coverage-html:
	pytest --cov-report html --cov=src tests/