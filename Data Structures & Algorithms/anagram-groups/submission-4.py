class Solution:



    def hash(self,s:str)->tuple:
        freq=[0]*26
        for c in s:
            freq[ord(c)-ord('a')]+=1
        return tuple(freq)



        
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)

        for s in strs:
            hmap[self.hash(s)].append(s)
        return [arr for arr in hmap.values()]




        