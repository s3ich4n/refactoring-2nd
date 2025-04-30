from datetime import datetime, timedelta


class Photo:
    def __init__(self, title, location, date):
        self.title = title
        self.location = location
        self.date = date


class Person:
    def __init__(self, name, photo):
        self.name = name
        self.photo = photo


def render_photo(out_stream, photo):
    """사진을 HTML로 렌더링합니다."""
    out_stream.write(f"<img src='photos/{photo.title}.jpg' />\n")


def recent_date_cutoff():
    """최근 날짜 기준점을 반환합니다 (현재 날짜에서 30일 전)."""
    return datetime.now() - timedelta(days=30)


def render_person(out_stream, person):
    """사람 정보를 HTML로 렌더링합니다."""
    out_stream.write(f"<p>{person.name}</p>\n")
    render_photo(out_stream, person.photo)
    emit_photo_data(out_stream, person.photo)


def list_recent_photos(out_stream, photos):
    """최근 사진 목록을 HTML로 렌더링합니다."""
    for p in [p for p in photos if p.date > recent_date_cutoff()]:
        out_stream.write("<div>\n")
        emit_photo_data(out_stream, p)
        out_stream.write("</div>\n")


def emit_photo_data(out_stream, photo):
    """사진 데이터를 HTML로 출력합니다."""
    zztmp(out_stream, photo)
    out_stream.write(f"<p>location: {photo.location}</p>\n")


def zztmp(out_stream, photo):
    out_stream.write(f"<p>title: {photo.title}</p>\n")
    out_stream.write(f"<p>date: {photo.date.strftime('%a %b %d %Y')}</p>\n")
