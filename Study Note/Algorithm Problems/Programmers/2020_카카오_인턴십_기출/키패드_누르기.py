def solution(numbers, hand):
    answer = ''
    
    left_nums = {1: 0, 4: 1, 7: 2}
    right_nums = {3: 0, 6: 1, 9: 2}
    mid_nums = {2: 0, 5: 1, 8: 2, 0: 3}
    
    left_cur = (3, 0)
    right_cur = (3, 2)
    for n in numbers:
        if n in left_nums.keys():
            answer += 'L'
            left_cur = (left_nums[n], 0)
        elif n in right_nums.keys():
            answer += 'R'
            right_cur = (right_nums[n], 2)
        else:
            num = (mid_nums[n], 1)
            ld = abs(left_cur[0] - num[0]) + abs(left_cur[1] - num[1])
            rd = abs(right_cur[0] - num[0]) + abs(right_cur[1] - num[1])
            if ld > rd:
                answer += 'R'
                right_cur = num
            elif ld < rd or hand == 'left':
                answer += 'L'
                left_cur = num
            else:
                answer += 'R'
                right_cur = num
                
    return answer