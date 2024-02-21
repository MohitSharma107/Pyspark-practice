"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""
"""

def removeVowels(s: str) -> str:
        return "".join(i for i in s if i not in {'a','e','i','o','u'})
        

print(removeVowels("leetcodeisacommunityforcoders"))
            
