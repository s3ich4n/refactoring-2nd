import json
import locale
from math import floor

with open("plays.json", "r") as f:
    plays = json.loads(f.read())

with open("invoices.json", "r") as f:
    invoices = json.loads(f.read())


def create_statement_data(invoice, plays):
    def total_amount(data):
        return sum(perf["amount"] for perf in data)

    def total_volume_credits(data):
        return sum(perf["volume_credits"] for perf in data)

    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance["audience"] - 30, 0)

        if "comedy" == a_performance["play"]["type"]:
            result += floor(a_performance["audience"] / 5)

        return result

    def amount_for(a_performance):
        result = 0

        match a_performance["play"]["type"]:
            case "tragedy":
                result = 40000
                if a_performance["audience"] > 30:
                    result += 1000 * (a_performance["audience"] - 30)

            case "comedy":
                result = 30000
                if a_performance["audience"] > 20:
                    result += 10000 + 500 * (a_performance["audience"] - 20)

                result += 300 * a_performance["audience"]

            case _:
                raise Exception(f"알 수 없는 장르: {a_performance['type']}")

        return result

    def play_for(a_performance):
        return plays[a_performance["playID"]]

    def enrich_performance(performance):
        """(limited) immutability for `play` data

        :param performance:
        :return:
        """
        result = performance.copy()  # shallow copy
        result["play"] = play_for(result)
        result["amount"] = amount_for(result)
        result["volume_credits"] = volume_credits_for(result)
        return result  # total_amount와 total_volume_credits 제거

    performances = [
        enrich_performance(performance) for performance in invoice[0]["performances"]
    ]
    statement_data = {
        "customer": invoice[0]["customer"],
        "performances": performances,
        "total_amount": total_amount(performances),
        "total_volume_credits": total_volume_credits(performances),
    }
    return statement_data


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
