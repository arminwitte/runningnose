from simpleexperimenttracker.simpleexperimenttracker import SimpleExperimentTracker 

def test_simpleexperimenttracker():
    tracker = SimpleExperimentTracker()
    assert isinstance(tracker, SimpleExperimentTracker)
    assert isinstance(tracker.job_name, str)
    assert len(tracker.job_name) == 24
