# Testing of service.

.PHONY: test

test:
	PYTHONPATH=. pytest -q

# Installation of Python and dependencies.

VENV=.venv
PYTHON=python3
PIP=$(VENV)/bin/pip
PY=$(VENV)/bin/python

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install -r requirements.txt

# Running and building Docker image.

build:
	docker build -t lynxelele/python-ml-test:local-dev .

run:
	docker run -d \
		-p 8000:8000 \
		-e PORT=8000 \
		lynxelele/python-ml-test:local-dev