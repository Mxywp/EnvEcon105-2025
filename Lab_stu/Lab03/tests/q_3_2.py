from otter.test_files import test_case

OK_FORMAT = False

name = "q_3_2"
points = None

@test_case(points=None, hidden=False)
def test_q_3_2(ekc_wide):
    assert 'CO2_emissionstons per capita)' not in ekc_wide.columns

