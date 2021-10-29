import math
li = [1, .6, 0, .8, .0, 1, 0, 0, 0, 0, 0, 0, .2, 0]
li = [[i, li[i-1]] for i in range(1,15)]

# calculate CG
def Cal_CG(l):
    for i in range(1,len(l)+1):
        CG = 0
        for j in range(i):
            CG += l[j][1]
        l[i-1].append(round(CG, 2))

    return l

# calculate CDG
def Cal_DCG(l):
    for i in range(1,len(l) + 1):
        _log = math.log(l[i-1][0], 2)
        l[i-1].append(round(_log, 2))

    for i in range(1, len(l) + 1):
        DCG = l[0][1]
        for j in range(1,i):
            DCG += l[j][1]/l[j][3]
        l[i-1].append(round(DCG, 2))

    return l

def reIndex(l):
    for i in range(1, len(l) + 1):
        l[i-1][0] = i
    return l

li = Cal_CG(li)
import copy

li_idcg = copy.deepcopy(li)
li_idcg = sorted(li_idcg, key=lambda l:l[1], reverse=True)
li_idcg = reIndex(li_idcg)
    
# calculate NDCG
li_idcg = Cal_DCG(li_idcg)
li = Cal_DCG(li)

def cal_NDCG(l1, l2):
    for i in range(len(li)):
        l1[i].append(l2[i][-1])
        l1[i].append(round(l1[i][-1]/l2[i][-1], 2))
    return sorted(l1, key=lambda l:l[0])

li = cal_NDCG(li, li_idcg)
# print("---------------------")
for i in range(len(li)):
    print(li[i])
