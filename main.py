# Press the green button in the gutter to run the script.
from typing import List

from GroupMaker import build_groups
from WordPair import WordPair


def print_results(sentence1: str, sentence2: str) -> None:
    pairs: List[WordPair] = build_groups(sentence1, sentence2)

    top_matches = list(map(lambda pair: pair.find_top_allowed_match_or_empty(), pairs))
    print(top_matches)


if __name__ == '__main__':
    print_results("prasidės nauja ryt kelione", "ryt Nauja kelionė prasids")

    print_results("As esu", "a As a es")

    print_results("Justas", "ir Justs")

    print_results("Aš esu Justas", "As ne esu justas")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
