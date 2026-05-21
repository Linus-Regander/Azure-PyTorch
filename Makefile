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
	docker run --rm -p 8000:8000 \
		-e SERVICE_NAME="Azure ML Svc" \
		-e SERVICE_VERSION="1.0.0" \
		-e SERVICE_HOST="0.0.0.0" \
		-e SERVICE_PORT="8000" \
		lynxelele/python-ml-test:local-dev