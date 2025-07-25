from otter.test_files import test_case

OK_FORMAT = False

name = "q_3_3"
points = None

@test_case(points=None, hidden=False)
def test_q_3_3(ekc_wide):
    assert 'CO2_tonpc' in ekc_wide.columns
    assert 'GDP_pc' in ekc_wide.columns
    assert 'PM25_mcgpcm' in ekc_wide.columns
    assert 'pop_den' in ekc_wide.columns

