eng_num = int(raw_input())
eng_list = raw_input().split()
eng_set = set(map(int, eng_list))
fren_num = int(raw_input())
fren_list = raw_input().split()
fren_set = set(map(int, fren_list))

print len(eng_set.union(fren_set))
