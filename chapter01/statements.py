import json
import locale

from chapter01.create_statement_data import create_statement_data

with open("plays.json", "r") as f:
    plays = json.loads(f.read())

with open("invoices.json", "r") as f:
    invoices = json.loads(f.read())


def html_statement(invoice, plays):
    return render_html(create_statement_data(invoice, plays))


def render_html(data):
    def usd(a_number):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        return locale.currency(a_number / 100, grouping=True)

    result = f"<h1>청구 내역 (고객명: {data['customer']})</h1>\n"
    result += "<table>\n"
    result += "<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>\n"

    for perf in data["performances"]:
        result += (
            f" <tr><td>{perf['play']['name']}</td>"
            f"<td>{perf['audience']}</td>"
            f"<td>{usd(perf['amount'])}</td></tr>\n"
        )

    result += "</table>\n"
    result += f"<p>총액: <em>{usd(data['total_amount'])}</em></p>\n"
    result += f"<p>적립 포인트: <em>{data['total_volume_credits']}</em> credits</p>\n"

    return result


def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice, plays))


def render_plain_text(data):
    def usd(a_number):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        return locale.currency(a_number / 100, grouping=True)

    result = f"청구 내역 (고객명: {data['customer']})\n"
    for perf in data["performances"]:
        result += (
            f" {perf['play']['name']}: {usd(perf['amount'])} {perf['audience']}석\n"
        )
    result += f"총액: {usd(data['total_amount'])}\n"
    result += f"적립 포인트: {data['total_volume_credits']}점\n"
    return result
