import json
import locale
from math import floor

with open("plays.json", "r") as f:
    plays = json.loads(f.read())

with open("invoices.json", "r") as f:
    invoices = json.loads(f.read())


def statement(invoice, plays):
    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance["audience"] - 30, 0)

        if "comedy" == a_performance["play"]["type"]:
            result += floor(a_performance["audience"] / 5)

        return result

    def amount_for(a_performance):
        """calculate amount for a play.

        I also put this method as a nested function
        to follow the approach of this book.

        :param a_performance:
        :param play:
        :return:
        """
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
        result = performance.copy()  # shallow copy
        result["play"] = play_for(result)
        result["amount"] = amount_for(result)
        result["volume_credits"] = volume_credits_for(result)
        return result

    statement_data = {
        "customer": invoice[0]["customer"],
        "performances": [
            enrich_performance(performance)
            for performance in invoice[0]["performances"]
        ],
    }
    return render_plain_text(statement_data)


def render_plain_text(data):
    def total_amount():
        result = 0
        for perf in data["performances"]:
            result += perf["amount"]

        return result

    def total_volume_credits():
        result = 0
        for perf in data["performances"]:
            result += perf["volume_credits"]
        return result

    def usd(a_number):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        return locale.currency(a_number / 100, grouping=True)

    result = f"청구 내역 (고객명: {data['customer']})\n"
    for perf in data["performances"]:
        result += (
            f" {perf['play']['name']}: {usd(perf['amount'])} {perf['audience']}석\n"
        )
    result += f"총액: {usd(total_amount())}\n"
    result += f"적립 포인트: {total_volume_credits()}점\n"
    return result


if __name__ == "__main__":
    result = statement(invoices, plays)
    print(result)
