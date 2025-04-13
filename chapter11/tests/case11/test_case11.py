from collections import namedtuple

from chapter11.src.case11.case11 import calculate_ascent

# 테스트를 위한 간단한 Point 클래스
Point = namedtuple("Point", ["elevation"])


class TestCalculateAscent:
    def test_calculate_ascent_with_ascending_points(self):
        # 상승하는 포인트들
        points = [
            Point(elevation=100),
            Point(elevation=150),
            Point(elevation=200),
            Point(elevation=250),
        ]

        assert calculate_ascent(points) == 150  # 50 + 50 + 50

    def test_calculate_ascent_with_descending_points(self):
        # 하강하는 포인트들
        points = [
            Point(elevation=300),
            Point(elevation=250),
            Point(elevation=200),
            Point(elevation=150),
        ]

        assert calculate_ascent(points) == 0  # 모든 변화가 음수

    def test_calculate_ascent_with_mixed_points(self):
        # 상승과 하강이 혼합된 포인트들
        points = [
            Point(elevation=100),
            Point(elevation=150),  # +50
            Point(elevation=120),  # -30 (무시)
            Point(elevation=180),  # +60
            Point(elevation=150),  # -30 (무시)
            Point(elevation=200),  # +50
        ]

        assert calculate_ascent(points) == 160  # 50 + 60 + 50

    def test_calculate_ascent_with_empty_points(self):
        # 빈 포인트 리스트
        points = []

        assert calculate_ascent(points) == 0

    def test_calculate_ascent_with_single_point(self):
        # 포인트가 하나뿐인 경우
        points = [Point(elevation=100)]

        assert calculate_ascent(points) == 0
