from chapter11.src.case06.case06 import (
    HeatingPlan,
    Thermostat,
    adjust_temperature,
)


class TestHeatingPlan:
    """
    HeatingPlan 클래스를 테스트하는 클래스
    """

    def test_target_temperature(self):
        """
        target_temperature 메서드 테스트
        """
        # 테스트를 위한 설정
        stat = Thermostat(22, 20)
        heating_plan = HeatingPlan(18, 25)

        # 정상 범위 내의 온도
        assert heating_plan.target_temperature(stat.selected_temperature) == 22

        # 최대 온도 초과
        stat = Thermostat(28, 20)
        assert heating_plan.target_temperature(stat.selected_temperature) == 25

        # 최소 온도 미만
        stat = Thermostat(15, 20)
        assert heating_plan.target_temperature(stat.selected_temperature) == 18

    def test_adjust_temperature(self, capsys):
        """
        adjust_temperature 함수 테스트
        """
        # 난방 테스트 (목표 온도 > 현재 온도)
        stat = Thermostat(22, 20)
        heating_plan = HeatingPlan(18, 25)
        adjust_temperature(stat, heating_plan)
        captured = capsys.readouterr()
        assert captured.out.strip() == "난방 켜기"

        # 냉방 테스트 (목표 온도 < 현재 온도)
        stat = Thermostat(22, 24)
        adjust_temperature(stat, heating_plan)
        captured = capsys.readouterr()
        assert captured.out.strip() == "냉방 켜기"

        # 끄기 테스트 (목표 온도 = 현재 온도)
        stat = Thermostat(22, 22)
        adjust_temperature(stat, heating_plan)
        captured = capsys.readouterr()
        assert captured.out.strip() == "온도 조절 시스템 끄기"
