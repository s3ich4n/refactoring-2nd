.PHONY: test test-all clean clean-coverage clean-results combine-coverage merge-junit

CHAPTERS = chapter01 chapter04 chapter06 chapter07 chapter09
TEST_RESULTS_DIR = test-results
COVERAGE_DIR = $(TEST_RESULTS_DIR)/coverage
JUNIT_DIR = $(TEST_RESULTS_DIR)/junit

# Poetry 환경 강제
POETRY ?= poetry run

test: test-all

clean: clean-results clean-coverage
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

clean-results:
	rm -rf $(TEST_RESULTS_DIR)

clean-coverage:
	$(POETRY) coverage erase
	rm -f $(COVERAGE_DIR)/.coverage*

test-all: clean-results clean-coverage $(TEST_RESULTS_DIR) run-all combine-coverage merge-junit

run-all:
	@for chapter in $(CHAPTERS); do \
		echo "Running tests for $$chapter..."; \
		(cd $$chapter && \
		COVERAGE_FILE=../$(COVERAGE_DIR)/.coverage.$$chapter \
		$(POETRY) coverage run -m pytest -v \
		--junitxml=../$(JUNIT_DIR)/$$chapter-results.xml) || exit $$?; \
	done

combine-coverage:
	$(POETRY) coverage combine $(COVERAGE_DIR)
	$(POETRY) coverage report
	$(POETRY) coverage html

merge-junit:
	$(POETRY) python -m pip show junitparser > /dev/null || $(POETRY) python -m pip install junitparser
	$(POETRY) python -m junitparser merge \
		$(JUNIT_DIR)/*.xml \
		$(TEST_RESULTS_DIR)/merged-results.xml

$(TEST_RESULTS_DIR):
	mkdir -p $(COVERAGE_DIR) $(JUNIT_DIR)
