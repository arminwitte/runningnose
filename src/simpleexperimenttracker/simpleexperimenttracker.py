import wonderwords
import datetime
import random

FAMOUS_SCIENTISTS = [
    # Female Scientists
    "Marie Curie",
    "Rosalind Franklin",
    "Ada Lovelace",
    "Jane Goodall",
    "Rachel Carson",
    "Dorothy Hodgkin",
    "Katherine Johnson",
    "Barbara McClintock",
    "Lise Meitner",
    "Vera Rubin",
    
    # Male Scientists
    "Albert Einstein",
    "Isaac Newton",
    "Galileo Galilei",
    "Charles Darwin",
    "Nikola Tesla",
    "Stephen Hawking",
    "Richard Feynman",
    "Niels Bohr",
    "Michael Faraday",
    "Alan Turing",

    # Female Scientists
    "Hypatia",
    "Emmy Noether",
    "Chien-Shiung Wu",
    "Mae Jemison",
    "Tu Youyou",
    "Maria Goeppert Mayer",
    "Rita Levi-Montalcini",
    "Gerty Cori",
    "Mary Anning",
    "Irene Joliot-Curie", #Sorry Irène, for the accent
    
    # Male Scientists
    "Gregor Mendel",
    "James Clerk Maxwell",
    "Louis Pasteur",
    "Carl Linnaeus",
    "Erwin Schroedinger", # Sorry Erwin, for the ö
    "Paul Dirac",
    "Linus Pauling",
    "Carl Sagan",
    "Jonas Salk",
    "Tim Berners-Lee"
]

class SimpleExperimentTracker:
    def __init__(self):
        self.job_name = self._job_name()
        self.experiment_name = random.choice(FAMOUS_SCIENTISTS).replace(" ", "_")
        pass

    def _job_name(self, name=None):
        if name is None:
            now = str(datetime.datetime.now().isoformat())
            date = now.split("T")[0]

            r = wonderwords.RandomWord()
            adjective = r.word(include_parts_of_speech=["adjectives"], word_min_length=3, word_max_length=8)
            length = 12 - len(adjective)
            noun = r.word(include_parts_of_speech=["nouns"], word_min_length=length, word_max_length=length)
            name = "_".join((date, adjective, noun))

        name = self._printable(name)
        return name
    @staticmethod
    def _printable(s):
        s_ = ''.join(s for s in myStr if s in string.printable)
        return s_
