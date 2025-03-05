.PHONY: test test-ch01 test-ch04 test-ch06 test-ch07 clean

test-all: test-ch01 test-ch04 test-ch06 test-ch07

test-ch01:
	cd chapter01 && pytest && cd ..

test-ch04:
	cd chapter04 && pytest && cd ..

test-ch06:
	cd chapter06 && pytest && cd ..

test-ch07:
	cd chapter07 && pytest && cd ..

# 모든 테스트의 alias
test: test-all

# 캐시 파일 정리
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
