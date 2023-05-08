"""Main functions"""


def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    string = string.replace(" ", "").replace("!", "").lower()
    for i in range(len(string)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
