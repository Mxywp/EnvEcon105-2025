from otter.test_files import test_case

OK_FORMAT = False

name = "q_2_1"
points = None

@test_case(points=None, hidden=False)
def test_q_2_1(N_rows, N_cols):
    assert N_rows in [860, 885]
    assert N_cols in [1, 5]

