
import re

lc = "LCNO-APN-70-2022-1001"

res = re.match(r'LCNO-(KAR|MAH|TAL|TND|APN|GOA)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})'
               r'-([0-9]{4})', lc)
if res :


    print("match found" )
    print(res.group(0))
else:
    print("no match found")
