class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicts={}
        for i in ransomNote:
            if i not in  dicts:
                dicts[i]=1
            else:
                occr =dicts.get(i)+1
                dicts[i]=occr
        print(dicts)
        for key in dicts:
            cnt = dicts[key]
            if magazine.count(key)<cnt:
                return False
            
        return True
