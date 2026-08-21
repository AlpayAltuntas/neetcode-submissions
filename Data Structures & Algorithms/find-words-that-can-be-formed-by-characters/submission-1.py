class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCount = Counter(chars)
        res = 0
        for word in words:
            wordCount = Counter(word)
            if all(wordCount[c] <= charCount[c] for c in wordCount):
                res += len(word)
        return res
            

        