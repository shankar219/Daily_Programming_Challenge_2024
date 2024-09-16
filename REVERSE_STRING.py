def reverse_words(s: str) -> str:
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    
    j = len(s) - 1
    while j >= 0 and s[j] == ' ':
        j -= 1

    words = []
    word = ''
    while i <= j:
        if s[i] != ' ':
            word += s[i]
        else:
            if word:
                words.append(word)
                word = ''
            while i <= j and s[i] == ' ':
                i += 1
            continue
        i += 1
    if word:
        words.append(word)
    
    reversed_words = ''
    for k in range(len(words)-1, -1, -1):
        reversed_words += words[k]
        if k != 0:
            reversed_words += ' '
    
    return reversed_words

s = input("Enter the string: ")
print(reverse_words(s))