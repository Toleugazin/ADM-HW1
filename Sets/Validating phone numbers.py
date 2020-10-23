import re
for i in range(int(raw_input())):
    print 'YES' if re.search(r"^[789]\d{9}$",raw_input()) else 'NO'
