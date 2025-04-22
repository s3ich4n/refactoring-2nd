from chapter08.src.case01.case01_1 import track_summary


def test_track_summary_calculation():
    """테스트를 위한 샘플 포인트 데이터로 track_summary 함수 테스트"""
    # 테스트를 위한 샘플 포인트 데이터
    points = [
        {"lat": 37.7749, "lon": -122.4194},  # San Francisco
        {"lat": 34.0522, "lon": -118.2437},  # Los Angeles
        {"lat": 36.7783, "lon": -119.4179},  # Fresno
    ]

    # track_summary 함수 호출
    result = track_summary(points)

    # 결과가 예상한 키를 포함하는지 검증
    assert "time" in result
    assert "distance" in result
    assert "pace" in result

    # 결과 값이 올바른 타입인지 검증
    assert isinstance(result["time"], (int, float))
    assert isinstance(result["distance"], (int, float))
    assert isinstance(result["pace"], (int, float))

    # 거리가 0보다 큰지 검증
    assert result["distance"] > 0


# 추가 테스트: 거리 계산 정확성 테스트
def test_zero_distance():
    """동일한 위치에 대한 거리 계산 테스트"""
    # 동일한 위치의 포인트
    points = [
        {"lat": 37.7749, "lon": -122.4194},  # San Francisco
        {"lat": 37.7749, "lon": -122.4194},  # 동일한 위치
    ]

    result = track_summary(points)

    # 거의 0에 가까운 거리가 계산되어야 함 (오차 허용)
    assert result["distance"] < 0.001
