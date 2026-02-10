from multiprocessing.util import spawnv_passfds

lis = [2,5,9,1]
lis.append(7)
lis.insert(2,3)
#lis.sort(reverse=True)
lis.sort()

#lis.remove(2)

print(lis)

print(f'essa lista tem {len(lis)} elementos')