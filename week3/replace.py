s = str(input())
k = s.find(' ')
word1 = s[:k]
word2 = s[k + 1:]
print(word2, word1)
