FLAKE8_FLAGS=--ignore=E501,W503


test:
	python3 test/test_examples.py

.PHONY: test
