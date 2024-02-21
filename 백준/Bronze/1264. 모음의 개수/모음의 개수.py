while True:
    word = input()
    if word == '#':
        break

    cnt = 0
    for w in word:
        for j in w:
            if j in 'aeiouAEIOU':
                cnt += 1
    print(cnt)
