from random import randint
import pandas as pd
from data_mod.Datapoint import Datapoint


def get_fake_dataframe(n):
    return pd.DataFrame([datapoint.__dict__ for datapoint in fake_data(n)])


def fake_data(n):
    return [fake_datapoint() for _ in range(0, n)]


def fake_datapoint():
    attend_lecture_rate = randint(0, 5)
    attend_practice_rate = randint(0, 5)
    hours_studying = randint(0, 5)
    hours_exam_prep = randint(0, 5)
    group_session = randint(0, 5)
    problem_sets_done_rate = randint(0, 5)
    problem_sets_success_rate = randint(0, 5)

    return Datapoint(attend_lecture_rate,
                     attend_practice_rate,
                     hours_studying,
                     hours_exam_prep,
                     group_session,
                     problem_sets_done_rate,
                     problem_sets_success_rate
                     )
