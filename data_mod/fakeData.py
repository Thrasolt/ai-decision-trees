from random import randint
import pandas as pd
from data_mod.DataPoint import DataPoint, RANDOM_FORESTS


def get_fake_dataframe(n, success_type=RANDOM_FORESTS):
    return pd.DataFrame([data_point.to_dict() for data_point in fake_data(n, success_type)])


def fake_data(n, success_type=RANDOM_FORESTS):
    return [fake_data_point(success_type) for _ in range(0, n)]


def fake_data_point(success_type=RANDOM_FORESTS):
    attend_lecture_rate = randint(0, 5)
    attend_practice_rate = randint(0, 5)
    hours_studying = randint(0, 5)
    hours_exam_prep = randint(0, 5)
    group_session = randint(0, 5)
    problem_sets_done_rate = randint(0, 5)
    problem_sets_success_rate = randint(0, 5)

    return DataPoint(attend_lecture_rate,
                     attend_practice_rate,
                     hours_studying,
                     hours_exam_prep,
                     group_session,
                     problem_sets_done_rate,
                     problem_sets_success_rate,
                     success_type
                     )
