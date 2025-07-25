from otter.test_files import test_case

OK_FORMAT = False

name = "q_2_2"
points = None

@test_case(points=None, hidden=False)
def test_q_2_2_1(N_unique_countries):
    assert 210 < N_unique_countries < 225

