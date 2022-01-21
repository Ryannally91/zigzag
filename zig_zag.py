def solution(number):
    zig_zag=[] #1 =true, #0 =false
    for i in range(len(number)):
        if i < len(number)-2:
            if number[i] > number[i+1] < number[i+2] or  number[i] < number[i+1] > number[i+2]:
                zig_zag.append(1)
            else:
                zig_zag.append(0)
        else:
            break
    return zig_zag


#test
    # [1, 2, 1, 3, 4]   [1,1,0]
print(solution((1, 2, 3, 4)))