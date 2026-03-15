from thefuzz import fuzz


def match_strings_ratio(string_one: str, string_two: str) -> int:
    return fuzz.ratio(string_one, string_two)
