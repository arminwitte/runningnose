import wonderwords
import datetime

class SimpleExperimentTracker:
    def __init__(self):
        self.job_name = self._job_name()
        pass

    def _job_name(self):
        now = str(datetime.datetime.now().isoformat())
        date = now.split("T")[0]

        r = wonderwords.RandomWord()
        adjective = r.word(include_parts_of_speech=["adjectives"])

        # generate a random word between the length of 3 and 8 characters
        r.word(word_min_length=3, word_max_length=8)
        
