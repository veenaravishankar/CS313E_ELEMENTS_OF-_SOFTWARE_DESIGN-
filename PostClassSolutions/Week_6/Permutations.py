def permutation(lst,start, end):
    if start == end:
        print(lst)
    else:
        for i in range(start,end+1):
            #choose
            lst[start],lst[i] = lst[i],lst[start]
            #exploration
            permutation(lst,start+1,end)
            #unchoose
            lst[start], lst[i] = lst[i], lst[start]


permutation(['B','E','V'],0,2)
