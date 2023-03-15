#!/usr/bin/env python
# coding: utf-8

# In[2]:


alg = {
    "alg1": set(),
    "alg2": set(),
    "alg3": set(),
    "alg4": set(),
    "alg5": set(),
    "alg6": set(),
    "alg7": set(),
}


with open("./overlap_data.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        fields = line.strip("\n").split(" ")
        guid = fields[0]
        algid = fields[1]
        alg[algid].add(guid)


# In[3]:


for k, v in alg.items():
    print(f"Alg: {k} - {len(v)}")
    print(f"\tIntersection alg1 - {len(alg[k].intersection(alg['alg1']))}")
    print(f"\tIntersection alg2 - {len(alg[k].intersection(alg['alg2']))}")
    print(f"\tIntersection alg3 - {len(alg[k].intersection(alg['alg3']))}")
    print(f"\tIntersection alg4 - {len(alg[k].intersection(alg['alg4']))}")
    print(f"\tIntersection alg5 - {len(alg[k].intersection(alg['alg5']))}")
    print(f"\tIntersection alg6 - {len(alg[k].intersection(alg['alg6']))}")
    print(f"\tIntersection alg7 - {len(alg[k].intersection(alg['alg7']))}")


# In[ ]:




