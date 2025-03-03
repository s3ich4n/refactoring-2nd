from copy import deepcopy


class CustomerData:
    def __init__(self, data):
        self._data = data

    def set_usage(self, customer_id, year, month, amount):
        self._data[customer_id]["usages"][year][month] = amount

    def usage(self, customer_id, year, month):
        return self._data[customer_id]["usages"][year][month]

    def compare_usage(self, customer_id, later_year, month):
        later = self.usage(customer_id, later_year, month)
        earlier_year = str(int(later_year) - 1)
        earlier = self.usage(customer_id, earlier_year, month)

        return {
            "later_amount": later,
            "change": later - earlier,
        }

    def get_raw_data(self):
        return deepcopy(self._data)


# 전역 인스턴스
customer_data = None


def initialize_data(data):
    global customer_data
    customer_data = CustomerData(data)


def get_customer_data():
    return customer_data


def get_raw_data_of_customers():
    return customer_data.get_raw_data()


# 예제 데이터 초기화
raw_data = {
    "1920": {
        "name": "martin",
        "id": "1920",
        "usages": {
            "2016": {
                "1": 50,
                "2": 55,
                # remaining months of the year
            },
            "2015": {
                "1": 70,
                "2": 63,
                # remaining months of the year
            },
        },
    },
    "38673": {
        "name": "neal",
        "id": "38673",
        # more customers in a similar form
    },
}

# 데이터 초기화
initialize_data(raw_data)


# 이제 compare_usage는 CustomerData 클래스의 메서드를 사용합니다
def compare_usage(customer_id, later_year, month):
    return get_customer_data().compare_usage(customer_id, later_year, month)
