from otter.test_files import test_case

OK_FORMAT = False

name = "q_1"
points = None

@test_case(points=None, hidden=False)
def test_q_1(q_1):
    assert len(q_1) in [2, 3]
    assert 'fips' in q_1
    assert 'ACSTOTPOP' in q_1

