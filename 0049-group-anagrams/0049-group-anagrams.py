class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == None:
            return [[]]
        angrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in angrams:
                angrams[sorted_word].append(word)
            else:
                angrams[sorted_word] = [word]
        return list(angrams.values())
