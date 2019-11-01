s = str(input())
k = s.find('h')
t = s.rfind('h')
st = s[k + 1:t]
st = st.replace('h', 'H')
s = s[:k + 1] + st + s[t:]
print(s)
