import numpy as np

RULE_INDUCTION = "RULE_INDUCTION"
DECISION_TREES = "DECISION_TREES"
RANDOM_FORESTS = "RANDOM_FORESTS"
SUCCESS_TYPES = [RULE_INDUCTION, DECISION_TREES, RANDOM_FORESTS]


class DataPoint:

    def __init__(self,
                 attend_lecture_rate,
                 attend_practice_rate,
                 hours_studying,
                 hours_exam_prep,
                 group_session,
                 problem_sets_done_rate,
                 problem_sets_success_rate,
                 success_type=RANDOM_FORESTS):

        if success_type not in SUCCESS_TYPES:
            self.success_type = RANDOM_FORESTS
        else:
            self.success_type = success_type

        self.attend_lecture_rate = attend_lecture_rate
        self.attend_practice_rate = attend_practice_rate
        self.hours_studying=hours_studying
        self.hours_exam_prep=hours_exam_prep
        self.group_session=group_session
        self.problem_sets_done_rate=problem_sets_done_rate
        self.problem_sets_success_rate=problem_sets_success_rate

        self.success = self.calculate_success()

    def calculate_success(self):
        if self.success_type == RULE_INDUCTION:
            return self.calculate_rule_induction()
        if self.success_type == DECISION_TREES:
            return self.calculate_decision_tree()
        return self.calculate_random_forests()

    def calculate_rule_induction(self):
        if self.problem_sets_success_rate == 5:
            return 1
        if self.problem_sets_done_rate >= 4 and self.hours_studying >= 4 and self.attend_lecture_rate >= 4:
            return 2
        if self.problem_sets_done_rate >= 3 and self.hours_studying >= 3 and self.attend_lecture_rate >= 4:
            return 3
        if self.problem_sets_done_rate >= 3 and self.hours_studying >= 2 and self.attend_lecture_rate >= 3:
            return 4
        return 5

    def calculate_random_forests(self):
        values = self.to_values()
        weights = np.array([3, 3, 5, 5, 2, 7, 9])
        value = np.sum(values*weights)
        divisor = sum(weights*5)
        return int(round((value/divisor)*6))

    def calculate_decision_tree(self):
        values = self.to_values()
        weights = np.array([0,5,1,5,2,1,4])
        # weights = np.array([1,5,1,5,2,1,4])
        value = np.sum(values*weights)
        divisor = sum(weights*5)
        return int(round((value/divisor)*6))

    def __call__(self):
        return ','.join([str(v) for k, v in self.__dict__.items()])

    def to_dict(self):
        dic = self.__dict__
        #dic.pop("success_type")
        return dic

    def to_values(self):
        dic = self.__dict__
        dic.pop("success_type")
        return np.array([int(v) for k, v in dic.items()])
