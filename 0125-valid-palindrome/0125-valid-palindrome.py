class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        cleaned_word = re.sub(r'[^a-z0-9]', '', word)
        if cleaned_word == cleaned_word[::-1]:
            return True
        return False