from collections import deque


class Resource:
    """자원을 나타내는 클래스"""

    @staticmethod
    def create():
        """새로운 Resource 객체를 생성"""
        return Resource()


class ResourcePool:
    """리소스 풀을 관리하는 클래스"""

    def __init__(self):
        """ResourcePool 초기화"""
        self.available = deque()  # Java의 Deque에 해당하는 파이썬의 deque
        self.allocated = []  # Java의 List에 해당하는 파이썬의 list

    def get(self):
        """
        가용한 리소스를 반환하거나, 없는 경우 새로 생성하여 반환

        Returns:
            Resource: 할당된 리소스
        """
        if not self.available:
            result = Resource.create()
            self.allocated.append(result)
        else:
            result = self.available.pop()
            self.allocated.append(result)

        return result
