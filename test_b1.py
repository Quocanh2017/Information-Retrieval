doc = "breakthrough drug for schizophrenia,new schizophrenia drug, new approach for treatment of schizophrenia, new hopes for schizophrenia patients"
dict = {}
doc.replace(",", "")
doc = doc.split(' ')

for d in set(doc):
    dict[d] = doc.count(d)

print(dict)

# -------------------

docs = ["" for i in range(10)]
S = ""
for i in range(10):
    with open("Wiki Docs/" + str(i+1) + ".txt") as f:
        docs[i] = f.read()
        docs[i].replace(",","")
        docs[i].replace(".","")
        docs[i].replace("(","")
        docs[i].replace(")","")
    S += S + docs[i]

def _count(l):
    c = 0
    for i in range(len(l)):
        if l[i] > 0:
            c += 1
    return c

S = set(S.split(" "))
l_dict = {}
for s in S:
    l = []
    for i in range(10):
        l.append(docs[i].split(" ").count(s))
    l_dict[s] = l
    
print(_count(l_dict["in"]))

