class Solution:

    def matches(self, s1: str, s2: str ) -> bool:
        if s1 == "[" and s2 == "]":
            return True 
        elif s1 == "(" and s2 == ")":
            return True 
        elif s1 == "{" and s2 == "}":
            return True
         
        return False 

    def isValid(self, stuff: str) -> bool:
        
        crap = []

        for s in stuff: 
            if s == "[" or s == "(" or s == "{":
                crap.append(s)
            elif s == "]" or s == ")" or s == "}":
                if len(crap) == 0:
                    return False
    
                if self.matches(crap[-1], s):
                    crap.pop()
                else: 
                    return False
        
        if len(crap) == 0:
            return True 

        return False 