black:
	black src/*.py tests/*.py
coverage:
	pytest --cov=src tests/