"""
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
"""

def findWordsContaining( words: list[str], x: str) -> list[int]:
        x_in_words = []
        for idx, word in enumerate(words):
            if x in set(word):
                x_in_words.append(idx)
        return x_in_words


print(findWordsContaining(["leet","code"], "e")) # [0,1]