def render_person(out_stream, person):
    result = []
    result.append(f"<p>{person['name']}</p>")
    result.append(render_photo(person["photo"]))
    result.append(f"<p>title: {person['photo']['title']}</p>")
    result.append(emit_photo_data(person["photo"]))
    return "\n".join(result)


def render_photo(photo):
    return f"<div>\n<p>제목: {photo['title']}</p>\n</div>"


def photo_div(p):
    return "\n".join(
        [
            "<div>",
            emit_photo_data(p),
            "</div>",
        ]
    )


def emit_photo_data(p):
    return "\n".join(
        [
            f"<p>title: {p['title']}</p>",
            f"<p>location: {p['location']}</p>",
            f"<p>date: {p['date'].strftime('%Y-%m-%d')}</p>",
        ]
    )
