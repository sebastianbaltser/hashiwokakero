build:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

tests: 
	pytest src/tests
	