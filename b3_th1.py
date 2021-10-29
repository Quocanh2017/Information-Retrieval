# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:43:24 2021

@author: User
"""

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import open_dir
from whoosh.query import *
from whoosh.qparser import QueryParser
import os.path

#if not os.path.exists("index/test"):
#    os.mkdir("index/test")
    
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
# ix = create_in("index/test", schema)

path = "index/test"
ix = open_dir(path)

# dic = {
#        "First":"How can we write programs to access text from local files and from the web, in order to get hold of an unlimited range of language material",
#        "Second":"How can we split documents up into individual words and punctuation symbols, so we can carry out the same kinds of analysis we did with text corpora in earlier chapters",
#        "Third":"How can we write programs to produce formatted output and save it in a file",
#        "Fourth":"This was our first brush with the reality of the web: texts found on the web may contain unwanted material, and there may not be an automatic way to remove it",
#        "Fifth":"The web can be thought of as a huge corpus of unannotated text. Web search engines provide an efficient means of searching this large quantity of text for relevant linguistic examples",
#        "Sixth":"The main advantage of search engines is size: since you are searching such a large set of documents, you are more likely to find any linguistic pattern you are interested in"}
#
# l = ["//a","//b","//c","//d","//e","//f"]
# writer = ix.writer()
# for i,key in enumerate(dic):
#     writer.add_document(title=key, path=l[i], content=dic[key])
# writer.commit()
# ix.close()
#
# myQuery = And([Term("content","How"),
#                Term("content","How")])

inp = input("hoi di? ")

# myquery = And([Term("content", "How"), Term("content", "can")])

with ix.searcher() as searcher:
    if("or" not in inp):
        qp = QueryParser("content", schema=ix.schema).parse(inp)
    else:
        qp = QueryParser("content", schema=ix.schema).parse(inp.replace("or","OR"))
    results = searcher.search(qp)
    # if results == []:
    #     print("Khong co ket qua.")
    # else:
    for result in results:
        print("title: ", result['title'])
    # Yêu cầu người dùng chọn kết quả muốn xem chi tiết
    k = int(input('Which result do you want to show? '))
        
    # Mở và hiển thị nội dung file tương ứng với kết quả đã chọn
    # fp = open("text/" + results[k], 'r')
    # print()
    # print(fp.read())
    print(type(results))
    # print("ket qua: ", results.count())



