install:
	poetry install
gendiff:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
lint:
	poetry run flake8
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
test:
	poetry run pytest
diff:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
diff_plain:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml -f plain
diff_json:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml -f json
test:
	poetry run pytest