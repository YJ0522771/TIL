import sys
sys.stdin = open("input.txt", "r")

delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////
    N = int(input())
    atoms = []
    for _ in range(N):
        # x, y, d, k
        atoms.append(list(map(int, input().split())))
    for atom in atoms:
        atom[0] *= 2
        atom[1] *= 2

    res = 0
    while len(atoms) > 1:
        for atom in atoms:
            atom[0] += delta[atom[2]][0]
            atom[1] += delta[atom[2]][1]

        atoms.sort(key=lambda x: (x[0], x[1]))

        new = []
        ll = len(atoms)
        i = 0
        while i < ll:
            if atoms[i][0] < -2000 or atoms[i][0] > 2000 or atoms[i][1] < -2000 or atoms[i][1] > 2000:
                i += 1
                continue

            if i < ll - 1 and atoms[i][0] == atoms[i + 1][0] and atoms[i][1] == atoms[i + 1][1]:
                res += atoms[i][3]
                end = True
                for j in range(1, ll - i):
                    if atoms[i][0] == atoms[i + j][0] and atoms[i][1] == atoms[i + j][1]:
                        res += atoms[i + j][3]
                    else:
                        end = False
                        break
                if not end:
                    i += j
                else:
                    break
            else:
                new.append(atoms[i])
                i += 1
        atoms = new
        # print(new)

    print('#{} {}'.format(test_case, res))




