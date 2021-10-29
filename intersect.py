def intersect(p1, p2, hn=True):
    answer = []
    if hn:
        while (p1 != [] and p2 != []):
            if p1[0] == p2[0]:
                answer.append(p1[0])
                p1.pop(0)
                p2.pop(0)
            else:
                if len(p1) > len(p2):
                    p1.pop(0)
                else:
                    p2.pop(0)
    else:
        ax = max(len(p1), len(p2))
        mi = min(len(p1), len(p2))
        for i in range(ax):
            if ax == len(p1):
                if p1[i] not in p2:
                    answer.append(p1[i])
            else:
                if p2[i] not in p1:
                    answer.append(p2[i])
    return answer

def mul_intersect(*args):
    terms = [arg for arg in args]
    terms.sort()
    result = terms[0]
    terms.pop(0)
    while terms != [] and result != []:
        result = intersect(result, terms[0])
        terms.pop(0)
    return result

def query_or(p1, p2):
    answer = []
    while (p1 != [] and p2 != []):
        if p1[0] == p2[0]:
            answer.append(p1[0])
            p1.pop(0)
            p2.pop(0)
        else:
            if len(p1) > len(p2):
                answer.append(p1[0])
                p1.pop(0)
            else:
                answer.append(p2[0])
                p2.pop(0)  
    return answer

doc = ["text/doc1.txt", "text/doc2.txt", "text/doc3.txt", "text/doc4.txt"]
for i in range(len(doc)):
    with open(doc[i], "r") as f:
        doc[i] = f.read()
# print(doc1)
# l = [i for i in doc]
l = ["breakthrough drug for schizophrenia","new schizophrenia drug",
    "new approach for treatment of schizophrenia","new hopes for schizophrenia patients"]
    
x = []
for i in range(len(l)):
    x += l[i].split(" ")

s = sorted(set(x))
di = {}

for si in s:
    di[si] = [] 

for i,li in enumerate(l):
    y = li.split(" ")
    for j in range(len(y)):
        if y[j] in s:
            if i in di[y[j]]:
                continue
            di[y[j]].append(i)

print(di)

# ans = mul_intersect(di["the"],di["use"])
# ans2 = intersect(di["schizophrenia"],di["drug"])
# print(ans2)
# ans = intersect(di["schizophrenia"],di["drug"],False)
# print(ans)
