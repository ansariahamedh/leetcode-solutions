from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in strings:
                strings[key].append(string)
            else:
                strings[key] = [string]
        return list(strings.values())