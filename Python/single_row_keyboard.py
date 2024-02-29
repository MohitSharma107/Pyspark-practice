def calculateTime(keyboard: str, word: str) -> int:
    keyboard_dict = {value: idx for idx, value in enumerate(keyboard)}
    res = 0
    previous_idx = 0
    for char in word:
        res += abs(keyboard_dict[char] - previous_idx)
        previous_idx = keyboard_dict[char]
    return res

print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
    

        