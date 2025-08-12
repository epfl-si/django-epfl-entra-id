.PHONY: help
help: ## Display this help message
	@echo "Please use make <target> where <target> is one of"
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-15s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Remove coverage reports and build artifacts
	@rm -fr htmlcov/
	@rm -f coverage.xml .coverage
	@rm -fr .pdm-build/
	@rm -fr dist/
	@rm -fr .tox/

.PHONY: lint
lint: ## Check coding style
	tox -e lint

.PHONY: test
test: ## Run tests on every supported Python/Django combination
	tox
