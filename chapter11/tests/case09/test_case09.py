from unittest.mock import MagicMock

from chapter11.src.case09.case09 import score


class TestScore:
    def test_score_with_smoker_and_low_certification(self):
        # 테스트를 위한 Mock 객체 설정
        candidate = MagicMock()
        candidate.origin_state = "low_state"

        medical_exam = MagicMock()
        medical_exam.is_smoker = True

        scoring_guide = MagicMock()
        scoring_guide.state_with_low_certification.return_value = True

        # 함수 실행
        result = score(candidate, medical_exam, scoring_guide)

        # 기대 결과: -5(낮은 인증) - 5(건강 수준 10-5) = -10
        assert result == -10

    def test_score_with_non_smoker_and_regular_certification(self):
        # 테스트를 위한 Mock 객체 설정
        candidate = MagicMock()
        candidate.origin_state = "regular_state"

        medical_exam = MagicMock()
        medical_exam.is_smoker = False

        scoring_guide = MagicMock()
        scoring_guide.state_with_low_certification.return_value = False

        # 함수 실행
        result = score(candidate, medical_exam, scoring_guide)

        # 기대 결과: 0(기본 점수) - 0(건강 수준 0-5, 음수이므로 max는 0) = 0
        assert result == 0

    def test_score_with_smoker_and_regular_certification(self):
        # 테스트를 위한 Mock 객체 설정
        candidate = MagicMock()
        candidate.origin_state = "regular_state"

        medical_exam = MagicMock()
        medical_exam.is_smoker = True

        scoring_guide = MagicMock()
        scoring_guide.state_with_low_certification.return_value = False

        # 함수 실행
        result = score(candidate, medical_exam, scoring_guide)

        # 기대 결과: 0(기본 점수) - 5(건강 수준 10-5) = -5
        assert result == -5
