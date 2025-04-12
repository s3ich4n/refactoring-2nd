class Thermostat:
    def __init__(self, selected_temperature, current_temperature):
        self.selected_temperature = selected_temperature
        self.current_temperature = current_temperature


class HeatingPlan:
    def __init__(self, min_temp, max_temp):
        self.min = min_temp
        self.max = max_temp

    def target_temperature(self):
        selected_temperature = thermostat.selected_temperature

        if selected_temperature > self.max:
            return self.max
        elif selected_temperature < self.min:
            return self.min
        else:
            return selected_temperature


# 클라이언트 코드
def adjust_temperature(thermostat, the_plan):
    if the_plan.target_temperature() > thermostat.current_temperature:
        set_to_heat()
    elif the_plan.target_temperature() < thermostat.current_temperature:
        set_to_cool()
    else:
        set_off()


def set_to_heat():
    print("난방 켜기")


def set_to_cool():
    print("냉방 켜기")


def set_off():
    print("온도 조절 시스템 끄기")


# 전역 변수 thermostat - 원래 자바스크립트 코드의 전역 참조를 모방
thermostat: Thermostat | None = None
