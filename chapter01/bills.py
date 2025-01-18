import json
import locale
from math import floor

with open("plays.json", "r") as f:
    plays = json.loads(f.read())

with open("invoices.json", "r") as f:
    invoices = json.loads(f.read())


def statement(invoice, plays):
    statement_data = {}
    return render_plain_text(statement_data, invoice, plays)


def render_plain_text(data, invoice, plays):
    def total_amount():
        result = 0
        for perf in invoice[0]["performances"]:
            result += amount_for(perf)

        return result

    def total_volume_credits():
        result = 0
        for perf in invoice[0]["performances"]:
            result += volume_credits_for(perf)
        return result

    def volume_credits_for(a_performance):
        volume_credits = 0
        volume_credits += max(a_performance["audience"] - 30, 0)

        if "comedy" == play_for(a_performance)["type"]:
            volume_credits += floor(a_performance["audience"] / 5)

        return volume_credits

    def usd(a_number):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        return locale.currency(a_number / 100, grouping=True)

    def play_for(a_performance):
        return plays[a_performance["playID"]]

    def amount_for(a_performance):
        """calculate amount for a play.

        I also put this method as a nested function
        to follow the approach of this book.

        :param a_performance:
        :param play:
        :return:
        """
        result = 0

        match play_for(a_performance)["type"]:
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
                raise Exception(f"알 수 없는 장르: {play_for(a_performance)['type']}")

        return result

    result = f"청구 내역 (고객명: {invoice[0]['customer']})\n"
    for perf in invoice[0]["performances"]:
        result += (
            f" {play_for(perf)['name']}: {usd(amount_for(perf))} {perf['audience']}석\n"
        )
    result += f"총액: {usd(total_amount())}\n"
    result += f"적립 포인트: {total_volume_credits()}점\n"
    return result


if __name__ == "__main__":
    result = statement(invoices, plays)
    print(result)
