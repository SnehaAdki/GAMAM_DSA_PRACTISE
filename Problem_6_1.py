#approach 2 to find the longest substring palindrome

def lon_sub_sring(s):
    val_long=""

    if len(s) <=1:
        return s
    for  i in range(len(s)):
        for j in range(i+1,len(s)):
            n_v = s[i:j]
            if n_v == n_v[::-1] and len(n_v)>len(val_long):
                val_long = n_v

    else:
        if val_long == '':
            return s[0]

    return val_long
