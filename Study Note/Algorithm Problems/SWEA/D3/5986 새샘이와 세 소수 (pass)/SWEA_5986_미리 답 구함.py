import sys
sys.stdin = open("input.txt", "r")

count = [0, 0, 0, 1, 2, 2, 2, 3, 4, 3, 5, 5, 5, 7, 7, 6, 9, 8, 9, 10, 11, 10, 12, 13, 12, 15, 16, 14, 17, 16, 16, 19, 21, 20, 20, 22, 21, 22, 28, 24, 25, 29, 27, 29, 33, 29, 33, 35, 34, 30, 38, 36, 35, 43, 38, 37, 47, 42, 43, 50, 46, 
47, 53, 50, 45, 57, 54, 47, 62, 53, 49, 65, 59, 55, 68, 61, 60, 69, 68, 58, 77, 73, 60, 78, 69, 65, 89, 75, 69, 86, 80, 75, 92, 90, 74, 95, 91, 73, 102, 93, 82, 107, 95, 85, 110, 100, 95, 116, 111, 88, 122, 115, 90, 125, 114, 
94, 130, 111, 102, 132, 124, 109, 134, 134, 108, 142, 137, 108, 154, 136, 111, 154, 139, 120, 157, 149, 127, 158, 160, 122, 171, 166, 129, 176, 161, 134, 186, 159, 143, 187, 171, 146, 190, 187, 143, 198, 190, 146, 210, 187, 151, 210, 186, 161, 207, 197, 167, 213, 207, 161, 234, 216, 162, 237, 211, 170, 244, 210, 180, 240, 225, 182, 238, 
239, 183, 254, 241, 181, 267, 231, 195, 278, 234, 200, 269, 255, 209, 271, 270, 200, 287, 273, 197, 294, 270, 215, 300, 260, 222, 297, 278, 231, 304, 298, 220, 318, 305, 219, 336, 299, 229, 336, 290, 245, 330, 318, 258, 321, 328, 247, 352, 334, 250, 369, 330, 260, 373, 330, 267, 377, 352, 275, 362, 367, 269, 388, 380, 268, 394, 362, 283, 408, 357, 294, 412, 374, 311, 400, 402, 293, 430, 410, 291, 440, 399, 309, 442, 395, 319, 434, 412, 332, 434, 426, 326, 467, 437, 313, 476, 428, 328, 484, 423, 337, 483, 443, 355, 463, 466, 346, 489, 472, 337, 505, 462, 360, 
522, 442, 366, 515, 478, 377, 505, 501, 363, 537, 508, 359, 547, 510, 387, 547, 486, 396, 557, 514, 417, 550, 531, 393, 583, 546, 386, 597, 542, 406, 604, 523, 426, 597, 565, 440, 574, 585, 426, 616, 589, 418, 646, 572, 443, 650, 561, 456, 651, 605, 459, 624, 628, 454, 667, 644, 444, 674, 623, 468, 693, 585, 500, 694, 631, 498, 669, 664, 479, 713, 683, 460, 727, 662, 496, 740, 640, 516, 718, 678, 526, 706, 702, 523, 759, 706, 504, 768, 701, 522, 798, 682, 547, 777, 714, 558, 745, 762, 547, 778, 758, 524, 810, 742, 567, 832, 705, 574, 821, 772, 578, 789, 801, 
564, 845, 801, 546, 848, 795, 589, 855, 762, 601, 863, 810, 633, 840, 825, 605, 889, 858, 584, 910, 842, 619, 918, 796, 627, 911, 865, 657, 856, 893, 638, 933, 891, 627, 968, 864, 651, 971, 860, 666, 974, 917, 675, 924, 930, 660, 989, 945, 647, 988, 923, 689, 1007, 890, 715, 1034, 941, 716, 959, 988, 700, 1047, 1002, 669, 1054, 956, 717, 1060, 946, 738, 1033, 998, 755, 1012, 1029, 744, 1097, 1017, 701, 1105, 1009, 758, 1112, 976, 756, 1109, 1036, 790, 1056, 1095, 769]
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    print('#{} {}'.format(test_case, count[N//2]))