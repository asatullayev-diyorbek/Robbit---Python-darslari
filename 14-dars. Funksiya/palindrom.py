def isPalindrome(string: str) -> bool:
    return string.lower() == string[::-1].lower()
