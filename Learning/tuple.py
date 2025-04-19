def tuple_yu(tupla: tuple):
    pass

if __name__ == "__main__":
    months = (
    'January', 'February', "March", "April", "May", "June",
    "July", 'August', 'September', 'October', 'November','December'
    )
    print(months)
    print(months.count("August"))
    print(months.index("March"))
    baroque = ("Vivaldi",)
    new_tuple = months + baroque
    print(new_tuple)
    list_tuple = [
                ('January', 30), ('February', 28), ('March', 31), ('April', 30),
                ('May', 31), ('June', 30), ('July', 31), ('August', 30),
                ]
    print(list_tuple[7][1])
    print([list_tuple[i][0] for i in range(len(list_tuple))])
    print(sorted(months))
    print(sorted(months, reverse=True))
    num_tuple = (0, 1, 2, 3, 4, 5)
    print(min(num_tuple))
    print(max(num_tuple))
    print(num_tuple[1:3])

    tuple_packed = ("final fantasy", "Ronin", "333")
    game, movie, fav_num = tuple_packed
    print("Unpacked data: {0}, {1}, {2}".format(game, movie, fav_num))
    
    ##########################
    tuple_=(1,3,4,5,6)
    print(tuple_)

    tuple_=(7,8,9)
    print(tuple_)

    list_=[i for i in range(10)]
    list_[0]=0
    list_.append(10)
    list_.append(11)
    list_=list_+list_[2:4]
    print(list_)

    tuple_ = tuple(list_[:])
    tuple_= tuple_+tuple_
    print(tuple_)
    print(list_)

    ##########################

    import random

    # create a Tuple
    tuple_ = tuple()
    print(tuple_)
    tuple1 = (5)
    print(tuple1)
    list_ = [5, 3, 2, 5, 7, 8, 4]
    tuple2 = tuple(list_)
    print(tuple2, "counts for 5: ", tuple2.count(5), ", index at 8: ",tuple2.index(8), ", length of tuple: ",tuple2.__len__(), len(tuple2))
    print("adding 4 to tuple1:",tuple1.__add__(4))
    print("adding 3 to tuple1:",tuple1+3)
    print("printing tuple1, no change: ", tuple1)
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    print(months)
    print(months[7])
    NPC=[("Valeria", 89), ("Voldo", 133), ("Connan", 450)]
    print(NPC)
    print(NPC[2])
    print(NPC[1][0])
    print(NPC[0][1])
    print()
    for element in NPC:
        print(element)
    print()
    #Unpacking ONLY for tuples
    tuple3=("Valeria", 9)
    print(tuple3)
    print("After unpacking")
    (name, score)=tuple3
    print(name," ", score)
    print("Unpacking", NPC)

    for tuple_elem in NPC:
        (name, score)=tuple_elem
        print("name",NPC.index(tuple_elem)," ",name)
        print("score",NPC.index(tuple_elem)," ",score)
        print()
    
    # Accessing locations within a tuple
    print(NPC[-3][0])
    print(NPC[0][-2])
    print(NPC[-2])
    print(NPC[:-1])
    print(NPC[-3:])

    # getting max and min numbers with tuple
    tuple4=(random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90))
    print(tuple4)
    print(tuple4[0:3])
    print(max(tuple4))
    print(min(tuple4))

    