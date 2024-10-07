class Solution:
    def groupAnagrams(self):
        check = {}
        alls=[]
        for i in strs:
            splits = list(i)
            print(splits)
            alls.append(splits)
        return alls

strs =["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(strs))