from simpleexperimenttracker.simpleexperimenttracker import SimpleExperimentTracker 

def test_simpleexperimenttracker():
    tracker = SimpleExperimentTracker()
    assert isinstance(tracker, sit.SimpleExperimentTracker)
