

# ---------- INSTALL ----------
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# ---------- TEST ----------
test: test-unit # Run entire test suite

test-unit: # Run unit tests
	pytest tests

# ---------- RUN ----------
run-app:
	python3.8 -m trafikboxen
