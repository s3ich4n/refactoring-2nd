import json
import locale
from math import floor

with open("plays.json", "r") as f:
    plays = json.loads(f.read())

with open("invoices.json", "r") as f:
    invoices = json.loads(f.read())


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"청구 내역 (고객명: {invoice[0]['customer']})\n"

    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    format = lambda x: locale.currency(x, grouping=True)

    for perf in invoice[0]["performances"]:
        play = plays[perf["playID"]]
        this_amount = 0

        # Replaced switch because python does not support switch case.
        # I prefer to use pattern matching(PEP 636)
        # see also: https://peps.python.org/pep-0636/
        match play["type"]:
            case "tragedy":
                this_amount = 40000
                if perf["audience"] > 30:
                    this_amount += 1000 * (perf["audience"] - 30)

            case "comedy":
                this_amount = 30000
                if perf["audience"] > 20:
                    this_amount += 10000 + 500 * (perf["audience"] - 20)

                this_amount += 300 * perf["audience"]

            case _:
                raise Exception(f"알 수 없는 장르: {perf['type']}")

        volume_credits += max(perf["audience"] - 30, 0)

        if "comedy" == play["type"]:
            volume_credits += floor(perf["audience"] / 5)

        result += f" {play['name']}: {format(this_amount / 100)} {perf['audience']}석\n"
        total_amount += this_amount

    result += f"총액: {format(total_amount / 100)}\n"
    result += f"적립 포인트: {volume_credits}점\n"

    return result


if __name__ == "__main__":
    result = statement(invoices, plays)
    print(result)
