class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap -> key: sorted str, value: list of strings
        my_map = {}
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string not in my_map: my_map[sorted_string] = []
            my_map[sorted_string].append(string)
        return list(my_map.values())
        