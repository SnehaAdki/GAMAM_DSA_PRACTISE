def lon_sub_sring(string):
    if len(string) <= 1:
        return string
    

    LBS = ""

    for i in range(1,len(string)):

        ## for odd string
        low = high = i
        while string[low] == string[high]:
            low -=1
            high +=1
        
            if low == -1 or high == len(string):
                break

        curr_pal = string[low+1:high]
        if len(curr_pal) > len(LBS):
            LBS = curr_pal


        ## even len

        low = i-1
        high = i

        while string[low] == string[high]:
            low-=1
            high+=1
            
            if low == -1 or high == len(string):
                break

        curr_pal = string[low+1:high]

        if len(curr_pal) > len(LBS):
            LBS = curr_pal

    return LBS


print(lon_sub_sring('abb'))
