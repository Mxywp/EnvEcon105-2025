from otter.test_files import test_case

OK_FORMAT = False

name = "q_2"
points = None

@test_case(points=None, hidden=False)
def test_q_2_1(q_2):
    assert len(q_2) in [13, 14]
    assert 'P_PNPL_D2' in q_2.index
    assert 'P_PM25_D2' in q_2.index
    assert 'P_CANCR_D2' in q_2.index

