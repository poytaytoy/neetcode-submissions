class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_string = [char.lower() for char in s if char.isalnum()]

        return cleaned_string[::-1] == cleaned_string 