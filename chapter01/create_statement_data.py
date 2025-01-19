from math import floor


class PerformanceCalculator:
    def __init__(
        self,
        a_performance,
        a_play,
    ):
        self.a_performance = a_performance
        self.play = a_play

    def amount(self):
        result = 0

        match self.play["type"]:
            case "tragedy":
                result = 40000
                if self.a_performance["audience"] > 30:
                    result += 1000 * (self.a_performance["audience"] - 30)

            case "comedy":
                result = 30000
                if self.a_performance["audience"] > 20:
                    result += 10000 + 500 * (self.a_performance["audience"] - 20)

                result += 300 * self.a_performance["audience"]

            case _:
                raise Exception(f"알 수 없는 장르: {self.play['type']}")

        return result


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

    def enrich_performance(a_performance):
        """(limited) immutability for `play` data

        :param a_performance:
        :return:
        """
        calc = PerformanceCalculator(a_performance, play_for(a_performance))
        result = a_performance.copy()  # shallow copy

        result["play"] = calc.play
        result["amount"] = calc.amount()
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
