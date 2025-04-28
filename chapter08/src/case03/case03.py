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
        ["<div>", f"<p>title: {p['title']}</p>", emit_photo_data(p), "</div>"]
    )


def emit_photo_data(a_photo):
    result = []
    result.append(f"<p>location: {a_photo['location']}</p>")
    result.append(f"<p>date: {a_photo['date'].strftime('%Y-%m-%d')}</p>")
    return "\n".join(result)
