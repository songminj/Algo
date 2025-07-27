import sys
input = sys.stdin.readline

vowel = {'a', 'e', 'i', 'o', 'u'}

def valuation(word: str):
    is_vowel = False
    for i in range(len(word)):
        w = word[i]
        # 1번 조건: 모음 포함
        if w in vowel:
            is_vowel = True
        # 3번 조건: 연속된 같은 글자 (ee, oo 예외)
        if i > 0 and word[i] == word[i - 1] and word[i] not in {'e', 'o'}:
            return f'<{word}> is not acceptable.'

    # 2번 조건: 모음 or 자음 3연속
    for i in range(len(word) - 2):
        a, b, c = word[i], word[i + 1], word[i + 2]
        if a in vowel and b in vowel and c in vowel:
            return f'<{word}> is not acceptable.'
        if a not in vowel and b not in vowel and c not in vowel:
            return f'<{word}> is not acceptable.'

    if not is_vowel:
        return f'<{word}> is not acceptable.'

    return f'<{word}> is acceptable.'

while True:
    word = input().strip()
    if word == 'end':
        break
    print(valuation(word))
