
PYTHON_FILES=$(shell find . -name '*.py')

static-check: static-check-codestyle-report static-check-pylint-report
#   static-check-typecheck

static-check-codestyle-report: $(PYTHON_FILES)
	python3 -m pycodestyle .

static-check-pylint-report: $(PYTHON_FILES)
	python3 -m pylint --rcfile .pylintrc $?
