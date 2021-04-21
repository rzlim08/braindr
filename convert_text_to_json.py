#!/usr/bin/env python
# coding: utf-8
import json 
with open("nki_func_dataset.txt", "r") as f:
    l = f.read().splitlines()
d = {}
for imname in l:
    d[imname.replace(".jpg", "")] = {"ave_score": 0, "num_votes": 0}
with open("full_nki_func.json", "w+") as f:
    json.dump(d, f, indent=4)
