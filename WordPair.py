from typing import List
import Levenshtein


class WordPair:
    max_levenshtein_distance_allowed = 1

    def __init__(self, word: str, possible_matches: List[str]):
        self.possibleMatches = possible_matches
        self.word = word

    def find_top_allowed_match_or_empty(self) -> (str, str):
        perfect: str = self.__perfect_match()
        if perfect is not None:
            return self.word, perfect
        close_allowed_match: str = self.find_closest_match_or_empty()
        return self.word, close_allowed_match

    def __perfect_match(self) -> str:
        return next((w for w in self.possibleMatches if w == self.word), None)

    def find_closest_match_or_empty(self):
        return next((w for w in self.possibleMatches if
                     Levenshtein.distance(self.word, w) <= self.max_levenshtein_distance_allowed), "")
