import arrow
from datetime import datetime

def kst_now() -> datetime:
    """ KST 기준의 현재시각을 리턴한다.

    Returns:
    """
    return arrow.now("Asia/Seoul").datetime
