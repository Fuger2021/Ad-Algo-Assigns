import numpy as np
from PIL import Image


def v(path4v, x_size, y_size, savepath):
    img = Image.new('RGB', (x_size + 1, y_size + 1), color='white')
    for node in path4v:
        img.putpixel(node, (0, 0, 0))
    rotated_img = img.rotate(-90, resample=Image.BICUBIC, expand=True)
    flipped_img = rotated_img.transpose(method=Image.FLIP_LEFT_RIGHT)
    flipped_img.save(savepath)


def gen_map(map_id):
    if map_id == 1:
        map_1 = np.zeros((14, 17))
        map_1[5][6] = map_1[6][6] = map_1[7][7] = map_1[8][7] = map_1[9][7] = map_1[9][8] = map_1[10][8] = map_1[11][8] = -1
        return map_1, 14, 17, (8, 4), (9, 13)

    elif map_id == 2:
        map_2 = np.zeros((20, 40))
        map_2[0][3] = -1
        for i in range(6):
            map_2[2][i] = -1
        map_2[0][7], map_2[1][7], map_2[2][7], map_2[2][8], map_2[2][9], map_2[2][10], map_2[3][8] = [-1] * 7
        for i in range(8):
            map_2[i][12] = -1
        for i in range(7):
            map_2[5][i] = -1
        map_2[7][5], map_2[8][5], map_2[9][5], map_2[10][5], map_2[11][5] = [-1] * 5
        map_2[11][4], map_2[11][3], map_2[11][2], map_2[10][2], map_2[12][3], map_2[13][3], map_2[14][3], map_2[15][3], map_2[16][3] = [-1] * 9
        map_2[15][4], map_2[15][5], map_2[15][6], map_2[15][7], map_2[15][8], map_2[14][8], map_2[13][8], map_2[13][9], map_2[12][8], \
        map_2[11][8], map_2[10][8], map_2[10][7], map_2[9][7] = [-1] * 13
        map_2[13][11], map_2[12][12], map_2[13][12], map_2[14][12], map_2[15][12], map_2[16][12], map_2[17][12], map_2[18][12], map_2[19][
            12] = [-1] * 9
        map_2[18][3], map_2[19][3], map_2[17][7], map_2[18][7], map_2[19][7], map_2[15][24], map_2[15][25], map_2[16][24], map_2[16][
            25] = [-1] * 9

        for i in range(10, 13):
            for j in range(19, 22):
                map_2[i][j] = -1

        map_2[10][28], map_2[11][31], map_2[13][31], map_2[7][36], map_2[9][36] = [-1] * 5
        for i in range(24, 40):
            map_2[0][i] = 4
        for i in range(25, 40):
            map_2[1][i] = 4
        for i in range(26, 40):
            map_2[2][i] = 4
        for i in range(26, 37):
            map_2[3][i] = 4
        for i in range(26, 36):
            map_2[4][i] = 4
        for i in range(27, 33):
            map_2[5][i] = 4
        for i in range(27, 33):
            map_2[6][i] = 4
        for i in range(29, 33):
            map_2[7][i] = 4
        map_2[1][34], map_2[2][33], map_2[3][32], map_2[4][33], map_2[5][33], map_2[5][34], map_2[6][33], map_2[6][34], map_2[7][33], \
        map_2[7][34], map_2[7][35] = [2] * 11
        map_2[8][32], map_2[8][33], map_2[8][34], map_2[8][35], map_2[9][32], map_2[9][33], map_2[9][34], map_2[10][32], map_2[10][33], \
        map_2[11][32] = [2] * 10
        map_2[10][36], map_2[10][35], map_2[11][35], map_2[11][34], map_2[12][34], map_2[12][33], map_2[13][34], map_2[13][33], map_2[13][
            32], map_2[14][34], map_2[14][33], map_2[14][32] = [2] * 12
        map_2[15][33], map_2[15][32], map_2[15][31], map_2[16][33], map_2[16][32], map_2[16][31], map_2[17][32], map_2[17][31], map_2[17][
            30] = [2] * 9
        map_2[18][31], map_2[18][30], map_2[18][29], map_2[19][30], map_2[19][29], map_2[19][28] = [2] * 6

        return map_2, 20, 40, (10, 4), (0, 35)
