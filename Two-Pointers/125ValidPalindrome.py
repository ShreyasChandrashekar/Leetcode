class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ""

        for k in s:
            if k.isalpha():
                res+=k.lower()
            elif k.isdigit():
                res+=str(k)

        l = 0
        r = len(res)-1

        while l < r:
            if res[l] != res[r]:
                return False
            l+=1
            r-=1
        
        return True