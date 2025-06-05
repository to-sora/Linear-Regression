import csv
import copy
import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from linearRegression import LinearRegression, use


def load_rows(path, n):
    data = []
    with open(path) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i >= n:
                break
            data.append([float(x) for x in row])
    return data


def test_use_does_not_modify_input_and_returns_expected_output():
    inp = [4.0]
    var = [2.0, 3.0]
    original = inp.copy()
    output = use(inp, var)
    assert output == pytest.approx(11.0)
    # ensure input list has not been modified
    assert inp == original


def test_training_reduces_error_on_small_dataset(tmp_path):
    data = load_rows('traindata.csv', 5)
    model = LinearRegression(copy.deepcopy(data), constant=1, errorpercent=False)
    before = model.testonvar(copy.deepcopy(data))
    before.analyze()
    before_error = before.avgRM2

    model.trainsimpleLR(epoch=10, learning_rate=0.1, learning_decay=False,
                        printable=False, selftest=False, showdot=0)

    after = model.testonvar(copy.deepcopy(data))
    after.analyze()
    after_error = after.avgRM2

    assert after_error < before_error
