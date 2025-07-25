from otter.test_files import test_case

OK_FORMAT = False

name = "q_3_1"
points = None

@test_case(points=None, hidden=False)
def test_q_3_1(ekc_wide):
    assert 'CO2 emissions (metric tons per capita)' in ekc_wide.columns
    assert 'CO2_emissionstons per capita)' in ekc_wide.columns
    assert 'GDP per capita (constant 2015 US$)' in ekc_wide.columns
    assert 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)' in ekc_wide.columns
    assert 'Population density (people per sq. km of land area)' in ekc_wide.columns

