import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

bst = BSTNode("Dan")
for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# the runtime for this approach is around 0.009
start_time = time.time()
# Remove duplicate values from names_1 and names_2
new_names1 = list(dict.fromkeys(names_1))
new_names2 = list(dict.fromkeys(names_2))
# merge to list
new_names = new_names1 + new_names2
# get duplicate values between names_1 and names_2
s = set()
duplicates2 = []
for name in new_names:
    if name not in s:
        s.add(name)
    else:
        duplicates2.append(name)

end_time = time.time()
print(f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
