class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # תנאי 1: שני המחרוזות חייבות להכיל את אותן אותיות בדיוק
        if set(word1) != set(word2):
            return False
        
        # תנאי 2: תדירות התווים צריכה להיות זהה מבחינת מספרי מופעים
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        return sorted(freq1.values()) == sorted(freq2.values())