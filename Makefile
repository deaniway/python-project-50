install:
	poetry install
gendiff:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-reinstall:
	 python3 -m pip install  --force-reinstall dist/*.whl
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
test:
	poetry run pytest
check:
	poetry run flake8 gendiff
	poetry run flake8 tests
	poetry run pytest