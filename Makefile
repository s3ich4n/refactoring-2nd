.PHONY: test test-all test-ch01 test-ch04 test-ch06 test-ch07 clean clean-coverage clean-results combine-coverage merge-junit

CHAPTERS = ch01 ch04 ch06 ch07
TEST_RESULTS_DIR = test-results

test: test-all

clean: clean-results clean-coverage
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

clean-results:
	rm -rf $(TEST_RESULTS_DIR)

clean-coverage:
	coverage erase
	rm -f $(TEST_RESULTS_DIR)/.coverage*

test-all: clean-results clean-coverage $(TEST_RESULTS_DIR) test-ch01 test-ch04 test-ch06 test-ch07 combine-coverage merge-junit

test-ch01:
	cd chapter01 && \
	COVERAGE_FILE=../$(TEST_RESULTS_DIR)/.coverage.ch01 coverage run -m pytest -v \
	    --junitxml=../$(TEST_RESULTS_DIR)/ch01-results.xml

test-ch04:
	cd chapter04 && \
	COVERAGE_FILE=../$(TEST_RESULTS_DIR)/.coverage.ch04 coverage run -m pytest -v \
	    --junitxml=../$(TEST_RESULTS_DIR)/ch04-results.xml

test-ch06:
	cd chapter06 && \
	COVERAGE_FILE=../$(TEST_RESULTS_DIR)/.coverage.ch06 coverage run -m pytest -v \
	    --junitxml=../$(TEST_RESULTS_DIR)/ch06-results.xml

test-ch07:
	cd chapter07 && \
	COVERAGE_FILE=../$(TEST_RESULTS_DIR)/.coverage.ch07 coverage run -m pytest -v \
	    --junitxml=../$(TEST_RESULTS_DIR)/ch07-results.xml

combine-coverage:
	coverage combine $(TEST_RESULTS_DIR)
	coverage report
	coverage html

merge-junit:
	command -v python3 > /dev/null && python3 -m pip show junitparser > /dev/null || python3 -m pip install junitparser
	python3 -m junitparser merge \
	    $(TEST_RESULTS_DIR)/ch01-results.xml \
	    $(TEST_RESULTS_DIR)/ch04-results.xml \
	    $(TEST_RESULTS_DIR)/ch06-results.xml \
	    $(TEST_RESULTS_DIR)/ch07-results.xml \
	    $(TEST_RESULTS_DIR)/merged-results.xml

$(TEST_RESULTS_DIR):
	mkdir -p $(TEST_RESULTS_DIR)
