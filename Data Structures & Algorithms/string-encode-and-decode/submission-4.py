class Solution:

    def encode(self, strs: List[str]) -> str:

        starter = "ñ"

        for stuff in strs:
            starter += stuff + "ñ"

        return starter 

    def decode(self, s: str) -> List[str]:
        if s == "ñ":
            return []
            
        return s[1:-1].split("ñ")
        