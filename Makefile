.venv/bin/activate: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

tests: 
	pytest src/tests

run: .venv/bin/activate
	.venv/bin/python3 src/__main__.py
