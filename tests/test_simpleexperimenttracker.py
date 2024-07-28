from simpleexperimenttracker.simpleexperimenttracker import SimpleExperimentTracker 

def test_simpleexperimenttracker():
    tracker = SimpleExperimentTracker()
    tracker.set_experiment()
    tracker.set_job()
    assert isinstance(tracker, SimpleExperimentTracker)
    assert isinstance(tracker.experiment_name, str)
    assert isinstance(tracker.job_name, str)
    assert len(tracker.job_name) == 24
