import numpy as np


class Datapoint:

    def __init__(self,
                 attend_lecture_rate,
                 attend_practice_rate,
                 hours_studying,
                 hours_exam_prep,
                 group_session,
                 problem_sets_done_rate,
                 problem_sets_success_rate):

        self.attend_lecture_rate=attend_lecture_rate
        self.attend_practice_rate=attend_practice_rate
        self.hours_studying=hours_studying
        self.hours_exam_prep=hours_exam_prep
        self.group_session=group_session
        self.problem_sets_done_rate=problem_sets_done_rate
        self.problem_sets_success_rate=problem_sets_success_rate

        self.success = self.calculate_success()

    def calculate_success(self):

        values = np.array([v for k, v in self.__dict__.items()])
        weights = np.array([3, 3, 5, 5, 2, 7, 9])
        value = np.sum(values*weights)
        divisor = sum(weights*5)
        return int(round((value/divisor)*6))

    def __call__(self):
        return ','.join([str(v) for k, v in self.__dict__.items()])
