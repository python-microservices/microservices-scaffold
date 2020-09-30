linter:
	pylint --rcfile=pylintrc project > pylintReport.txt
test: 
	export CONFIGMAP_FILE=tests/config-tests.yml
	tox
pre_coverage:
	coverage erase
post_coverage:
	coverage combine
	coverage report -m
	coverage html
coverage: 
	$(MAKE) pre_coverage
	$(MAKE) test
	$(MAKE) post_coverage
all:
	$(MAKE) linter
	$(MAKE) coverage