def get_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

def get_unique(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.difference(set2)

def get_all(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.union(set2)

def add_set():
    set1 = set()
    set2 = set()
    for i in range(0, 11, 2):
        set1.add(i)

    for i in range(1, 11, 2):
        set2.add(i)
    return (set1, set2)

if __name__ == "__main__":
    list1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
    list2 = ["THREE", "SEVEN", "EIGHT", "FOUR", "THREE"]
    print(get_common(list1, list2))
    print(get_unique(list1, list2))
    print(get_all(list1, list2))
    set1, set2 = add_set()
    print(f"set1 = {set1} \nset1 ={set2}")
    print(set1.union(set2))
    print(sorted(set1.union(set2), reverse=True))
    set3 = set1.copy()
    print("{} {} {}".format(set1, set2, set3))
    set3 = set3.clear()
    print(set3)
    arr = [88, 76, 23, 10, 28, 33, 88]
    set3 = set(arr)
    print(set3)
    set3.remove(23)
    print(set3)
    set3.discard(76)
    print(set3)
    set4 = set2.union(set3)
    print(f"set4= {set4}")
    print(f"set3= {set3}")
    print(set4.intersection(set3))
    print(set4.difference(set3))
    print(set3.difference(set4))
    print(set3.issubset(set4))
    print(set4.issuperset(set3))
    print(set4.symmetric_difference(set3))

    ################################
    set_=set()
    set_.add("one")
    set_.add("two")
    set_.add("three")
    print(set_)
    aset=set("one")
    print(aset)
    list_=["three", "four", "five", "four"]
    set_test = set(list_)
    print(set_test)
    new_set = set_test.difference(aset)
    print(new_set)

    for element in new_set:
        print(element)

    cSet= set_ | set_test
    dSet= set_ & set_test
    print(cSet)
    print(dSet)