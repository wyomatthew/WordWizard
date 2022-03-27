import re

class Frequencies(object):
    def __init__(self, min_len: int = 3, max_len: int = 15):
        """Constructor to build a tracker for word frequencies.
        
        Parameters
        ----------
        min_len: int
            minimum length of a word to be counted
        max_len: int
            maximum length of a word to be counted"""
        # initialize frequency dictionary
        self.freqs: dict[str, int] = dict()
        self.min_len = min_len
        self.max_len = max_len

    def add_freqs(self, doc: str) -> None:
        """Updates internal state of object with added frequencies from passed in
        document. Matc"""
        # clean passed in doc
        cleaned = self.clean_text(doc)

        # find all words in passed in doc
        pattern = r'\b[a-z]{{{}}}\b'.format(f'{self.min_len},{self.max_len}')
        matches = re.findall(pattern, cleaned)

        for match in matches:
            count = self.freqs.get(match, 0)
            self.freqs[match] = count + 1
    
    def get_freq_dict(self) -> "dict[str, int]":
        """Returns copy of internal frequency dictionary"""
        return self.freqs.copy()

    def get_freq_arr(self) -> "list[list]":
        """Returns copy of internal frequency dictionary as 2d array"""
        return list(self.freqs.items())

    @staticmethod
    def clean_text(doc: str) -> str:
        """Cleans passed in text to more easily permit reading of word frequencies"""
        cleaned = doc.lower().strip()
        return cleaned
    