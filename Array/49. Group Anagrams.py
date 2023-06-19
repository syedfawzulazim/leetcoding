from typing import List
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        # T-> M * nlogN
        # for x in strs:
        #     s = sorted(x)
        #     hashMap[tuple(s)].append(x)
        #     #s = "".join(sorted(x))
        #     #hashMap[s].append(x)

        # T-> M * N
        for x in strs:
            count = [0] * 26
            for i in x:
                count[ord(i) - ord('a')] += 1
            hashMap[tuple(count)].append(x)
    
        return hashMap.values()



S = Solution()
S.groupAnagrams(["eat","tea","tan","ate","nat","bat"])