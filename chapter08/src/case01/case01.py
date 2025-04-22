import math


def top_calculate_distance(points):
    def distance(p1, p2):
        # 두 지점 간의 거리를 계산 (하버사인 공식 사용)
        EARTH_RADIUS = 3959  # 마일 단위
        dlat = radians(p2["lat"] - p1["lat"])
        dlon = radians(p2["lon"] - p1["lon"])
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
            radians(p1["lat"])
        ) * math.cos(radians(p2["lat"])) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return EARTH_RADIUS * c

    def radians(degrees):
        # 각도를 라디안으로 변환
        return degrees * math.pi / 180

    result = 0
    for i in range(1, len(points)):
        result += distance(points[i - 1], points[i])
    return result


def track_summary(points):
    def calculate_distance():
        return top_calculate_distance(points)

    def calculate_time():
        # 현실적인 구현을 위해 총 소요 시간을 계산하는 간단한 예시
        # (여기서는 임의로 이동 거리에 따른 시간을 반환)
        return calculate_distance() * 10  # 마일당 10분 소요

    total_time = calculate_time()
    total_distance = calculate_distance()
    pace = total_time / 60 / total_distance if total_distance > 0 else 0
    return {"time": total_time, "distance": total_distance, "pace": pace}
