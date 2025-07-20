from otter.test_files import test_case

OK_FORMAT = False

name = "q_3"
points = None

@test_case(points=None, hidden=False)
def test_q_3_1(np, q_3):
    assert np.isclose(q_3, 1480, rtol=0.003)

