def BitmapHoles(strArr):
    # # code goes here
    holes_coord = []
    # get hole coord
    for i, row in enumerate(strArr):
        for j, c in enumerate(row):
            if c == "0":
                holes_coord.append([i, j])

    hole_count = 0

    seen = set()
    hole = set()
    f = True
    bm = dict()
    # print("meow")
    for i, row in enumerate(strArr):
        for j, c in enumerate(row):
            bm[(i, j)] = int(c)
    l_count = 0
    # print("meow")
    # for i, row in enumerate(strArr):
    #     for j, c in enumerate(row):
    for i in range(len(strArr)):
        for j in range(len(strArr[i])):
            stack = [(i, j)]
            while stack:
                coord = stack.pop()
                if coord not in seen:
                    l_count += 1
                    # print(l_count)
                    seen.add(coord)
                    if bm[(i, j)] == 0 and coord not in hole:
                        hole.add(coord)
                        if f:
                            hole_count += 1
                            f = False
                        if coord[0] - 1 >= 0 and (coord[0] - 1, coord[1]) not in seen:
                            stack.append((coord[0] - 1, coord[1]))

                        if coord[0] + 1 < len(strArr) and (coord[0] + 1, coord[1]) not in seen:
                            stack.append((coord[0] + 1, coord[1]))

                        if coord[1] - 1 >= 0 and (coord[0], coord[1] - 1) not in seen:
                            stack.append((coord[0], coord[1] - 1))

                        if coord[1] + 1 < len(strArr[0]) and (coord[0], coord[1] + 1) not in seen:
                            stack.append((coord[0], coord[1] + 1))
            f = True

    # print("meow")

    ##
    return hole_count


# keep this function call here 
print(BitmapHoles(["1011", "0010"]))