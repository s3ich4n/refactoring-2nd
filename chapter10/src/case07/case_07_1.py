def search_villains(people):
    """
    사람 목록에서 joker나 saruman을 검색하고 발견 시 경고를 보냅니다.

    Args:
        people: 검색할 사람들의 리스트
    """
    found = False
    for p in people:
        if not found:
            if p == "joker":
                send_alert(p)
                found = True
            if p == "saruman":
                send_alert()
                found = True


def send_alert(p):
    """경고를 보내는 함수"""
    print(f"ALERT: Villain found! - {p}")
