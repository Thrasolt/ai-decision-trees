import numpy as np


def predict(values):
    return np.array([predict_single(x[0], x[1], x[2], x[3], x[4], x[5], x[6]) for x in values])


def predict_single(
        attend_lecture_rate,
        attend_practice_rate,
        group_session,
        hours_exam_prep,
        hours_studying,
        problem_sets_done_rate,
        problem_sets_success_rate):
    if problem_sets_success_rate == 5:
        return 1
    if attend_lecture_rate == 4 and problem_sets_done_rate == 4 and hours_studying == 4 and problem_sets_success_rate!=5:
        return 2
    if hours_studying == 5 and problem_sets_done_rate == 5 and attend_lecture_rate == 4:
        return 2
    if hours_studying == 5 and attend_lecture_rate == 5 and problem_sets_done_rate == 5:
        return 2
    if problem_sets_done_rate == 4 and hours_studying == 5 and attend_lecture_rate == 4:
        return 2
    if attend_lecture_rate == 5 and hours_studying == 5 and problem_sets_done_rate == 4 and attend_practice_rate!=2:
        return 2
    if hours_studying == 4 and problem_sets_done_rate == 5 and attend_lecture_rate == 4:
        return 2
    if hours_studying == 4 and attend_lecture_rate == 5 and problem_sets_done_rate == 5 and problem_sets_success_rate!=5:
        return 2
    if attend_lecture_rate == 5 and attend_practice_rate == 0 and group_session == 1:
        return 2
    if hours_studying == 3 and problem_sets_done_rate == 5 and attend_lecture_rate == 4:
        return 3
    if hours_studying == 3 and problem_sets_done_rate == 4 and attend_lecture_rate == 5:
        return 3
    if problem_sets_done_rate == 3 and attend_lecture_rate == 5 and hours_studying == 3:
        return 3
    if hours_studying == 3 and problem_sets_done_rate == 4 and attend_lecture_rate == 4 and hours_exam_prep!=4:
        return 3
    if problem_sets_done_rate == 3 and hours_studying == 4 and attend_lecture_rate == 4:
        return 3
    if hours_studying == 3 and problem_sets_done_rate == 5 and attend_lecture_rate == 5 and problem_sets_success_rate!=5:
        return 3
    if problem_sets_done_rate == 3 and attend_lecture_rate == 5 and hours_studying == 5 and group_session!=3:
        return 3
    if problem_sets_done_rate == 3 and attend_lecture_rate == 4 and group_session == 2:
        return 3
    if problem_sets_done_rate == 3 and hours_studying == 4 and attend_lecture_rate == 5:
        return 3
    if problem_sets_done_rate == 3 and hours_studying == 5 and problem_sets_success_rate == 0 and attend_lecture_rate == 4:
        return 3
    if problem_sets_done_rate == 3 and attend_lecture_rate == 4 and hours_studying == 3:
        return 3
    if problem_sets_done_rate == 3 and problem_sets_success_rate == 1 and attend_lecture_rate == 4:
        return 3
    if attend_lecture_rate == 3 and problem_sets_done_rate == 5 and hours_studying == 2:
        return 4
    if attend_lecture_rate == 3 and problem_sets_success_rate == 2 and attend_practice_rate == 1:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 4 and hours_studying == 2:
        return 4
    if attend_lecture_rate == 3 and hours_studying == 5 and attend_practice_rate == 3:
        return 4
    if hours_studying == 2 and problem_sets_done_rate == 3 and attend_lecture_rate == 4:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 5 and hours_exam_prep == 4:
        return 4
    if hours_studying == 2 and problem_sets_done_rate == 4 and attend_lecture_rate == 4:
        return 4
    if hours_studying == 2 and attend_lecture_rate == 5 and attend_practice_rate == 2:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 3 and hours_studying == 2:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 4 and problem_sets_success_rate == 4:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 5 and problem_sets_success_rate == 1:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 5 and problem_sets_success_rate == 3:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 3 and hours_studying == 3 and group_session!=4:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 4 and group_session == 1 and hours_exam_prep!=4:
        return 4
    if hours_studying == 2 and attend_lecture_rate == 5 and problem_sets_done_rate == 3:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 3 and hours_studying == 4:
        return 4
    if hours_studying == 2 and attend_lecture_rate == 5 and problem_sets_done_rate == 4 and problem_sets_success_rate!=5:
        return 4
    if attend_lecture_rate == 3 and problem_sets_done_rate == 5 and hours_exam_prep == 0 and group_session!=4:
        return 4
    if problem_sets_done_rate == 5 and hours_studying == 2 and attend_lecture_rate == 4:
        return 4
    if attend_lecture_rate == 3 and hours_exam_prep == 2 and hours_studying == 5:
        return 4
    if attend_lecture_rate == 3 and group_session == 4 and attend_practice_rate == 4:
        return 4
    if problem_sets_done_rate == 5 and attend_lecture_rate == 3 and group_session == 2 and attend_practice_rate!=5:
        return 4
    if problem_sets_done_rate == 5 and attend_lecture_rate == 3 and hours_studying == 3 and hours_exam_prep!=5:
        return 4
    if hours_studying == 2 and attend_lecture_rate == 5 and group_session == 1 and attend_practice_rate!=5:
        return 4
    if problem_sets_done_rate == 2 and problem_sets_success_rate!=5:
        return 5
    if problem_sets_done_rate == 0 and problem_sets_success_rate!=5:
        return 5
    if problem_sets_done_rate == 1 and problem_sets_success_rate!=5:
        return 5
    if attend_lecture_rate == 2 and problem_sets_success_rate!=5:
        return 5
    if attend_lecture_rate == 0 and problem_sets_success_rate!=5:
        return 5
    if attend_lecture_rate == 1 and problem_sets_success_rate!=5:
        return 5
    if hours_studying == 0 and problem_sets_success_rate!=5:
        return 5
    if hours_studying == 1 and problem_sets_success_rate!=5:
        return 5
    return 5
