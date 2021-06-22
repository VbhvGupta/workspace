
def countRev (s):
    ln = len(s)
    if ln%2 :
        return -1
    top = 0
    count = 0
    for i in range(ln) :
        if top == ln-i :
            if s[i] == '{' :
                top -= 1
                count += 1
            elif s[i] == '}' :
                top -= 1
        elif s[i] == '}' and top == 0 :
            top+=1
            count += 1
        elif s[i] == '{' :
            top+=1
        elif s[i] == '}' and top > 0:
            top -= 1
        elif s[i] == '}' :
            top+=1
            count += 1
    return count


#  Driver Code Starts
t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))
#  Driver Code Ends
