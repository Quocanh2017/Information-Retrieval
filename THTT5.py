D = ["" for i in range(10)]

path = "Wiki Docs/"
for i in range(1,11):
    with open(path + str(i) + ".txt", "r") as f:
        D[i-1] = f.read()

def tf(word, doc):
    if("," in doc or "." in doc or "'" in doc):
        doc.replace(",","")
        doc.replace(".","")
        doc.replace("'","")
        doc = doc.lower().split(" ")
    l = []
    for i in set(word):
        l.append(doc.count(i))
    return l

def chuanhoa(v):
    import math
    dai = math.sqrt(sum(x**2 for x in v))
    for i in range(len(v)):
        try:
            v[i] = v[i]/dai
        except ZeroDivisionError: 
            v[i] = 0
    return v

def cosin(v1, v2):
    import math
    dai1 = math.sqrt(sum(x**2 for x in v1))
    dai2 = math.sqrt(sum(x**2 for x in v2))
    t = 0
    for i in range(len(v1)):
        t += v1[i]*v2[i]
    try:
        return t/(dai1*dai2)
    except ZeroDivisionError:
        return 0

term = input("input term: ").lower().split(" ")
# print("word: ", set(term))
li = []
# print(tf(term, term))
for i in range(len(D)):
    _tf = tf(term, D[i])
    print(f"Doc {i+1} {_tf}")
    ch = chuanhoa(_tf)
    # print(f"chuan hoa: {ch}")
    li.append(ch)

query = input("input query: ").lower().split(" ")
tf_of_query = tf(term, query) 
print("tf q: ", tf_of_query)
dic = {}
for i in range(len(li)):
    dic[i+1] = cosin(tf_of_query, li[i])
    # print(f"tt {i+1}: {cosin(tf_of_query, li[i])}")

dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
for key in dict:
    print("doc:",key, "value:", dict[key])
# print(dic)