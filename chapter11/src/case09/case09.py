def score(candidate, medical_exam, scoring_guide):
    return Scorer(candidate, medical_exam).execute(scoring_guide)


class Scorer:
    def __init__(self, candidate, medical_exam):
        """

        Args:
            candidate: 후보자 정보
            medical_exam: 의료 검사 결과
        """
        self._candidate = candidate
        self._medical_exam = medical_exam

    def execute(self, scoring_guide):
        """
        점수를 계산하는 함수

        Args:

            scoring_guide: 점수 가이드

        Returns:
            int: 계산된 점수
        """
        result = 0
        health_level = 0
        high_medical_risk_flag = False

        if self._medical_exam.is_smoker:
            health_level += 10
            high_medical_risk_flag = True

        certification_grade = "regular"
        if scoring_guide.state_with_low_certification(self._candidate.origin_state):
            certification_grade = "low"
            result -= 5

        # lots more code like this
        result -= max(health_level - 5, 0)

        return result
