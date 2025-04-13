from chapter11.src.case13.case13 import ResourcePool, Resource


class TestResourcePool:
    def setup_method(self):
        """각 테스트 메서드 실행 전에 호출되는 설정 메서드"""
        self.pool = ResourcePool()

    def test_get_when_no_available_resources(self):
        """가용 리소스가 없을 때 get 메서드 테스트"""
        # 초기 상태에서는 가용 리소스가 없음
        resource = self.pool.get()

        # 새 리소스가 생성되어야 함
        assert resource is not None
        assert isinstance(resource, Resource)

        # 할당된 리소스 목록에 추가되어야 함
        assert len(self.pool.allocated) == 1
        assert self.pool.allocated[0] == resource

        # 가용 리소스 목록은 여전히 비어 있어야 함
        assert len(self.pool.available) == 0

    def test_get_when_available_resources_exist(self):
        """가용 리소스가 있을 때 get 메서드 테스트"""
        # 미리 생성된 리소스를 가용 리소스 목록에 추가
        pre_existing_resource = Resource.create()
        self.pool.available.append(pre_existing_resource)

        # get 메서드 호출
        resource = self.pool.get()

        # 미리 생성된 리소스가 반환되어야 함
        assert resource == pre_existing_resource

        # 할당된 리소스 목록에 추가되어야 함
        assert len(self.pool.allocated) == 1
        assert self.pool.allocated[0] == resource

        # 가용 리소스 목록은 비어 있어야 함
        assert len(self.pool.available) == 0

    def test_get_multiple_resources(self):
        """여러 리소스를 연속으로 가져올 때 테스트"""
        # 미리 생성된 리소스 2개를 가용 리소스 목록에 추가
        resource1 = Resource.create()
        resource2 = Resource.create()
        self.pool.available.append(resource1)
        self.pool.available.append(resource2)

        # 첫 번째 get 호출 - resource2가 반환되어야 함 (스택 구조)
        first_resource = self.pool.get()
        assert first_resource == resource2

        # 두 번째 get 호출 - resource1이 반환되어야 함
        second_resource = self.pool.get()
        assert second_resource == resource1

        # 세 번째 get 호출 - 새 리소스가 생성되어야 함
        third_resource = self.pool.get()
        assert third_resource is not None
        assert third_resource != resource1
        assert third_resource != resource2

        # 할당된 리소스 목록에는 3개의 리소스가 있어야 함
        assert len(self.pool.allocated) == 3
        assert self.pool.allocated == [resource2, resource1, third_resource]
