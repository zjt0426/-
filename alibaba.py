# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

from collections import defaultdict
tmp_map = defaultdict(list)
n, m, k = map(int, input().split(' '))
for _ in range(k):
    people, x1, x2 = input().split(' ')
    tmp_map[people] = [(int(x1), int(x2))]
# print(tmp_map)
times = int(input())





def judgeoutput(people, action, pre):
    i, j = action
    if i <= 0 or i > n or j <= 0 or j > m:
        print('out of bounds!')
        tmp_map[people].append(pre)
        return
    for key in tmp_map.keys():
        # for val in tmp_map[key]:
        if action in tmp_map[key]:
            if people == key:
                tmp_map[key].append((i, j))
                # print(tmp_map[key])
                print('peaceful')
                break
            else:
                # 判断输赢
                if len(tmp_map[key]) > len(tmp_map[people]):
                    # print('oooo')
                    print('%s wins!' % (key))
                    for item in tmp_map[people]:
                        tmp_map[key].append(item)
                    tmp_map[people]=[]
                    # print(tmp_map)
                    break
                elif len(tmp_map[key]) < len(tmp_map[people]):
                    print('%s wins!' % (people))
                    # print('oooo')
                    for item in tmp_map[people]:
                        del tmp_map[key]
                        tmp_map[people].append(item)
                    break

                else:
                    whowin(people, key)
                    break

        else:
            print('vanguish!')
            tmp_map[people].append((i, j))
            break
    return

def whowin(a, b):  # 添加
    if a in b:
        print('%s wins!' % (a))
        for item in tmp_map[b]:
            tmp_map[a].append(item)
            print(tmp_map)
    if a < b:
        print('%s wins!' % (b))
        for item in tmp_map[a]:

            tmp_map[b].append(item)
    return


for time in range(times):

    people_, action = input().split(' ')
    # print(people_,action)
    # print(people_)
    # if people_ not in tmp_map.keys():
    #     print('unexisted empire.')
    # print(tmp_map)
    if tmp_map[people_]:
        pre = tmp_map[people_][-1]
        x, y = pre
        # print(x, y)
        if action == 'D':
            action = (x, y + 1)
        elif action == 'W':
            action = (x - 1, y)
        elif action == 'A':
            action = (x, y - 1)
        else:
            action = (x + 1, y)
        # print(action)
        judgeoutput(people_, action, pre)
    else:
        print('unexisted empire.')
# 3 3 2
# ranko 1 1
# kotori 2 2
# 5
# ranko D
# ranko W
# ranko A
# kotori W
# kotori W