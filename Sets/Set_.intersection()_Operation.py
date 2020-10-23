eng_num = int(raw_input())
eng_set = raw_input().split()
eng_set = set(map(int, eng_set))
fren_num = int(raw_input())
fren_set = raw_input().split()
fren_set = set(map(int, fren_set))

print len(eng_set.intersection(fren_set))
