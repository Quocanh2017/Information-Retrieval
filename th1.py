# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:44:41 2021

@author: User
"""
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.index import open_dir
from whoosh.query import *
import os.path

if not os.path.exists("index"):
    os.mkdir("index")
    
schema = Schema(title=TEXT, content=TEXT)
ix = create_in("index", schema)   

ix = open_dir("index")
print(ix)
 
print(os.getcwd())
print(os.listdir())

writer = ix.writer()
writer.add_document(title="My document",content="This is my document!")

writer.add_document(title="Second try", content="This is the second example.")

writer.add_document(title="Third time's the charm", content="Examples are many.")
writer.commit() # Phải gọi commit để kết thúc

myQuery = Or([Term("content","document"),
               Term("content","example"),
               Term("content","example")])
with ix.seacher() as seacher:
    results = seacher.search(myQuery)
    print(results[0])