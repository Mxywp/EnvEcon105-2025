from otter.test_files import test_case

OK_FORMAT = False

name = "q_4_1"
points = None

@test_case(points=None, hidden=False)
def test_q_4_1(ekc_no_missing):
    assert 160 < ekc_no_missing.shape[0] < 200
    assert 'Afghanistan' not in ekc_no_missing.index
    assert 'Aruba' not in ekc_no_missing.index

