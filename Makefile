build:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

tests: 
	pytest src/tests

run:
	.venv/bin/python3 src/__main__.py
