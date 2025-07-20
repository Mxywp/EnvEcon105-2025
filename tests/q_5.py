from otter.test_files import test_case

OK_FORMAT = False

name = "q_5"
points = None

@test_case(points=None, hidden=False)
def test_q_5_1(np, q_5):
    assert 22000 < q_5 < 25000

