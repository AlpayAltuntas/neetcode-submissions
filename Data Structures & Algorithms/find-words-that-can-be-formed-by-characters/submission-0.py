class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dict_count = {}
        for c in chars:
            dict_count[c] = dict_count.get(c, 0) + 1
        
        count = 0
        for i in words:
            dict_i = {}
            for j in i:
                dict_i[j] = dict_i.get(j, 0) + 1
            form = True
            for c in dict_i:
                if (dict_i[c] > dict_count.get(c,0)):
                    form = False
                    break
            if (form):
                count += len(i)

        return count