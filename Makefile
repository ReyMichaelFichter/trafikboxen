

# ---------- INSTALL ----------
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# ---------- RUN ----------
run-app:
	python3.8 -m trafikboxen
