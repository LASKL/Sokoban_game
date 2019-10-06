file = open('map.second.txt')
a = file.read()
map_list = list(a)
print(map_list)
print(a)
print(a.find('x'))
string_len = 0
i = 0
while map_list[i] != '\n':
    i = i + 1
print(i)
string_len = i + 1
pos_x_start = map_list.index('a')
pos_win = map_list.index('o')
while True:

    move = input()
    if move == 'w':
        pos_x_start = map_list.index('x')
        if map_list[pos_x_start - string_len] == '#':
            continue
        if map_list[pos_x_start - string_len] == 'a':
            if map_list[pos_x_start - 2 * string_len] == '#':
                continue
            map_list[pos_x_start] = ' '
            map_list[pos_x_start - string_len] = 'x'
            map_list[pos_x_start - string_len * 2] = 'a'
            continue
        map_list[pos_x_start] = ' '
        map_list[pos_x_start - string_len] = 'x'
    if move == 'a':
        pos_x_start = map_list.index('x')
        if map_list[pos_x_start - 1] == '#':
            continue
        if map_list[pos_x_start - 1] == 'a':
            if map_list[pos_x_start - 2] == '#':
                continue


        if map_list[pos_x_start - 1] == 'a':
            map_list[pos_x_start] = ' '
            map_list[pos_x_start - 1] = 'x'
            map_list[pos_x_start - 2] = 'a'
            continue

        map_list[pos_x_start] = ' '
        map_list[pos_x_start - 1] = 'x'

    if move == 's':
        pos_x_start = map_list.index('x')
        if map_list[pos_x_start + string_len] == '#':
            continue
        if map_list[pos_x_start + string_len] == 'a':
            if map_list[pos_x_start + string_len * 2] == '#':
                continue
            map_list[pos_x_start] = ' '
            map_list[pos_x_start + string_len] = 'x'
            map_list[pos_x_start + string_len * 2] = 'a'
            continue
        map_list[pos_x_start] = ' '
        map_list[pos_x_start + string_len] = 'x'

    if move == 'd':
        pos_x_start = map_list.index('x')
        if map_list[pos_x_start + 1] == '#':
            continue


        if map_list[pos_x_start + 1] == 'a':
            if map_list[pos_x_start + 2] == '#':
                continue
            map_list[pos_x_start] = ' '
            map_list[pos_x_start + 1] = 'x'
            map_list[pos_x_start + 2] = 'a'
            continue

        map_list[pos_x_start] = ' '
        map_list[pos_x_start + 1] = 'x'
    output = ''.join(map_list)
    print(output)
    if map_list.index('a') == pos_win:
        print('win!')
        break
    if map_list.index('x') != pos_win:
        map_list[pos_win] = 'o'



