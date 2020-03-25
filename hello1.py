#!/usr/bin/env python3
import re
def rearrange(name):
    res = re.search(r"^([\w .]*), ([\w .]*)$",name)
    if res is None:
       return name
    return "{} {}".format(res[2],res[1])
