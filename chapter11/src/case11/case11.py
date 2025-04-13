from collections import namedtuple

total_ascent = 0

# 테스트를 위한 간단한 Point 클래스
Point = namedtuple("Point", ["elevation"])


def calculate_ascent(points):
    global total_ascent
    for i in range(1, len(points)):
        vertical_change = points[i].elevation - points[i - 1].elevation
        total_ascent += vertical_change if vertical_change > 0 else 0

    return total_ascent
