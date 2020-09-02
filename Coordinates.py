class Point:
    def __init__(self, x_cor, y_cor, number):
        self.name = number
        self.x = x_cor
        self.y = y_cor
        self.state = 'empty'


def point_definer(square_length):
    point_names = []
    x_cor_square = [-2, -1, 0, 1, 2]
    y_cor_square = [-2, -1, 0, 1, 2]
    x_cor_tri = [-2, 0, 2, -1, 0, 1]
    y_cor_tri1 = [4, 3]
    y_cor_tri2 = [-4, -3]

    for y in range(5):
        for x in range(5):
            x_cor = (x_cor_square[x]) * square_length
            point = Point(x_cor, y_cor_square[y] * square_length, f'x{(y * 5) + (x + 1)}')
            point_names.append(point)

    for x in range(6):
        x_cor = (x_cor_tri[x] * square_length)
        if x < 3:
            y_cor = y_cor_tri1[0]
        else:
            y_cor = y_cor_tri1[1]
        point = Point(x_cor, y_cor * square_length, f'x{x + 26}')
        point_names.append(point)

    for x in range(6):
        x_cor = (x_cor_tri[x] * square_length)
        if x < 3:
            y_cor = y_cor_tri2[0]
        else:
            y_cor = y_cor_tri2[1]
        point = Point(x_cor, y_cor * square_length, f'x{x + 32}')
        point_names.append(point)

    return point_names


def white_screen_coordinates():
    # noinspection PyUnusedLocal
    white_player_initial_coordinates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 31, 32, 33, 34, 35, 36, 15, 16, 17, 18, 19, 20,
                                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    return white_player_initial_coordinates


''' black_possible_coordinates = {

    # Centre Square ( starts from bottom left)

    'x1': '-100,100',
    'x2': '-50,100',
    'x3': '0,100',
    'x4': '50,100',
    'x5': '100,100',
    'x6': '-100,50',
    'x7': '-50,50',
    'x8': '0,50',
    'x9': '50,50',
    'x10': '100,50',
    'x11': '-100,0',
    'x12': '-50,0',
    'x13': '0,0',
    'x14': '50,0',
    'x15': '100,0',
    'x16': '-100,-50',
    'x17': '-50,-50',
    'x18': '0,-50',
    'x19': '50,-50',
    'x20': '100,-50',
    'x21': '-100,-100',
    'x22': '-50,-100',
    'x23': '0,-100',
    'x24': '50,-100',
    'x25': '100,-100',

    # Triangle A (starts from bottom left)

    'x26': '-99.98,199.98',
    'x27': '0,200',
    'x28': '100.02,199.98',
    'x29': '-50,150',
    'x30': '0,150',
    'x31': '50,150',
}'''


def neighbouring_points_def(point_names):
    neighbouring_points = {
        point_names[0]: [1, 5],
        point_names[1]: [0, 2, 6],
        point_names[2]: [1, 3, 6, 7, 8, 34, 35, 36],
        point_names[3]: [2, 4, 8],
        point_names[4]: [3, 9],
        point_names[5]: [0, 6, 15],
        point_names[6]: [1, 2, 5, 7, 10, 11],
        point_names[7]: [2, 6, 8, 18],
        point_names[8]: [2, 3, 7, 9, 13, 14],
        point_names[9]: [4, 8, 14],
        point_names[10]: [5, 6, 11, 15, 16],
        point_names[11]: [6, 10, 12, 16],
        point_names[12]: [7, 11, 13, 17],
        point_names[13]: [8, 12, 14, 18],
        point_names[14]: [8, 9, 13, 18, 19],
        point_names[15]: [10, 16, 20],
        point_names[16]: [10, 11, 15, 17, 21, 22],
        point_names[17]: [12, 16, 18, 22],
        point_names[18]: [13, 14, 17, 19, 22, 23],
        point_names[19]: [14, 18, 24],
        point_names[20]: [15, 21],
        point_names[21]: [16, 20, 22],
        point_names[22]: [16, 17, 18, 21, 23, 28, 29, 30],
        point_names[23]: [18, 22, 24],
        point_names[24]: [19, 23],
        point_names[25]: [26, 28],
        point_names[26]: [25, 27, 29],
        point_names[27]: [26, 30],
        point_names[28]: [22, 25, 29],
        point_names[29]: [22, 26, 28, 30],
        point_names[30]: [22, 27, 29],
        point_names[31]: [32, 34],
        point_names[32]: [31, 33, 35],
        point_names[33]: [32, 36],
        point_names[34]: [3, 31, 35],
        point_names[35]: [3, 32, 34, 36],
        point_names[36]: [3, 33, 35]
    }
    return neighbouring_points


def valid_jump_moves_def(point_names):
    # noinspection PyUnusedLocal
    valid_jump_moves = {
        point_names[0]: [[1, 2], [5, 10]],
        point_names[1]: [[2, 3], [6, 11]],
        point_names[2]: [[1, 0], [3, 4], [6, 10], [7, 12], [8, 14], [34, 31], [35, 32], [36, 33]],
        point_names[3]: [[2, 1], [8, 13]],
        point_names[4]: [[3, 2], [9, 14]],
        point_names[5]: [[6, 7], [10, 15]],
        point_names[6]: [[7, 8], [11, 16], [2, 36]],
        point_names[7]: [[6, 5], [8, 9], [12, 17], [2, 35]],
        point_names[8]: [[7, 6], [13, 18], [2, 34]],
        point_names[9]: [[8, 7], [14, 19]],
        point_names[10]: [[5, 0], [6, 2], [11, 12], [15, 20], [16, 22]],
        point_names[11]: [[6, 1], [12, 13], [16, 21]],
        point_names[12]: [[7, 2], [11, 10], [13, 14], [17, 22]],
        point_names[13]: [[8, 3], [12, 11], [18, 23]],
        point_names[14]: [[8, 2], [9, 4], [13, 12], [18, 22], [19, 24]],
        point_names[15]: [[10, 5], [16, 17]],
        point_names[16]: [[11, 6], [17, 18], [22, 27]],
        point_names[17]: [[12, 7], [16, 15], [18, 19], [22, 29]],
        point_names[18]: [[13, 8], [17, 16], [22, 28]],
        point_names[19]: [[14, 9], [18, 17]],
        point_names[20]: [[15, 10], [21, 22]],
        point_names[21]: [[16, 11], [22, 23]],
        point_names[22]: [[16, 10], [17, 12], [18, 14], [21, 20], [23, 24], [28, 25], [29, 26], [30, 27]],
        point_names[23]: [[18, 13], [22, 21]],
        point_names[24]: [[19, 14], [23, 22]],
        point_names[25]: [[28, 22], [26, 27]],
        point_names[26]: [[29, 22]],
        point_names[27]: [[30, 22], [26, 25]],
        point_names[28]: [[22, 18], [29, 30]],
        point_names[29]: [[22, 17]],
        point_names[30]: [[22, 16], [29, 28]],
        point_names[31]: [[34, 2], [32, 33]],
        point_names[32]: [[35, 2]],
        point_names[33]: [[36, 2], [32, 31]],
        point_names[34]: [[2, 8], [35, 36]],
        point_names[35]: [[2, 7]],
        point_names[36]: [[2, 6], [35, 34]]
    }
    return valid_jump_moves
