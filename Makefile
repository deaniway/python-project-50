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
pytest:
	poetry run  pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
check: lint pytest
