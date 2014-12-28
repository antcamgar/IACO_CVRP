import random
import time

test_list = list()
test_dict = dict()
test_set = set()

exponent = 6

sample = random.sample(list(range(10**exponent)),10**exponent)

init = time.time()
for i in sample:
    test_list.append(i)
end = time.time()

print "list appending ->",end-init

init = time.time()
for i in sample:
    test_dict[i] = i
end = time.time()

print "dict assginement ->",end-init

init = time.time()
for i in sample:
    test_set.add(i)
end = time.time()

print "set adding ->",end-init



init = time.time()
for i in sample:
    i in test_dict
end = time.time()
print "dict accessing \"in\" operator ->",end-init

init = time.time()
for i in sample:
    i in test_set
end = time.time()
print "set accessing \"in\" operator ->",end-init

init = time.time()
for i in sample:
    i in test_list
end = time.time()
print "list accessing \"in\" operator ->",end-init




