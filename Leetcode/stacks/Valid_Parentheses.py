s = input()

st = []

for i in s:
    if i in ['(', '{', '[']:
        st.append(i)
    else:
        if not st:
            print('False')
            exit()
        if i == ')' and st[-1] != '(':
            print('False')
            exit()
        if i == '}' and st[-1] != '{':
            print('False')
            exit()
        if i == ']' and st[-1] != '[':
            print('False')
            exit()
        st.pop()

if st:
    print('False')
else:
    print('True')