list_ = [9, 12, 10, 8, 2, 4, 7, 5, 3, 1]
for j in range(len(list_)-1):
    for i in range(len(list_)-1):
        if list_[i] > list_[i+1]:
            list_[i], list_[i+1] = list_[i+1], list_[i]

print(list_)