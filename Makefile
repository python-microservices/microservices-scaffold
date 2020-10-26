export PYMS_CONFIGMAP_FILE=tests/config-tests.yml

default: all

clean_linter_report:
	[ -f pylintReport.txt ] && rm pylintReport.txt

linter: clean_linter_report
	pylint project/* > pylintReport.txt

test:
	tox

clean_coverage:
	coverage erase

generate_coverage_report:
	coverage combine
	coverage report -m
	coverage html

coverage: clean_coverage test generate_coverage_report

all: linter coverage
