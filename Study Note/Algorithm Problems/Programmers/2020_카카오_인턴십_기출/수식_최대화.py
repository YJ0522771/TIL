def solve(nums, opers, visit):
    global res
    if len(nums) == 1:
        temp = nums[0]
        if temp < 0:
            temp = abs(temp)
        if temp > res:
            res = temp
        return
    
    for i in range(3):
        if visit[i]:
            continue
        temp1 = []
        temp2 = []
        num1 = nums[0]
        j = 1
        for o in opers:
            num2 = nums[j]
            if o == oper[i]:
                if o == '+':
                    num1 += num2
                elif o == '-':
                    num1 -= num2
                else:
                    num1 *= num2
            else:
                temp2.append(o)
                temp1.append(num1)
                num1 = num2
            j += 1
        temp1.append(num1)
        # print(temp1)
        # print(temp2)
        visit[i] = True
        solve(temp1, temp2, visit)
        visit[i] = False
                
    
res = 0
oper = ['+', '-', '*']
def solution(expression):
    answer = 0
    
    nums = []
    opers = []
    num = 0
    for e in expression:
        if e in oper:
            nums.append(num)
            opers.append(e)
            num = 0
        else:
            num *= 10
            num += int(e)
    nums.append(num)

    solve(nums, opers, [False] * 3)
    answer = res
    
    return answer