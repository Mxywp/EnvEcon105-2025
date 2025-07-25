from otter.test_files import test_case

OK_FORMAT = False

name = "q_2_1"
points = None

@test_case(points=None, hidden=False)
def test_q_2_1(gdp_ekc):
    N_rows = gdp_ekc.shape[0]
    N_cols = gdp_ekc.shape[1]
    assert N_rows in [860, 885]
    assert N_cols in [1, 5]

