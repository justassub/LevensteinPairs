from typing import List

from WordPair import WordPair


def build_groups(sentence1: str, sentence2: str) -> List[WordPair]:
    list1: List[str] = sentence1.split(" ")
    list2: List[str] = sentence2.split(" ")
    return __make_groups(list1, list2)


def __make_groups(words1: List[str], words2: List[str]) -> List[WordPair]:
    longer_list: List[str] = words1 if len(words1) > len(words2) else words2
    shorter_list: List[str] = words2 if len(words1) > len(words2) else words1

    return list(map(lambda n: __make_word_pair(n, shorter_list), longer_list))


def __make_word_pair(word: str, possible_matches: List[str]) -> WordPair:
    return WordPair(word, possible_matches)
