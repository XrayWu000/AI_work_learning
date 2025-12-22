# 五子棋
# 1. 先把棋盤畫出來
# 2. 落子(落到最相鄰的位置)
# 3. 判斷落子是否五子
import pygame as pg

def check_win(board, x, y):
    player = board[x][y]

    # 四個方向向量 (dx, dy)
    directions = [
        (1, 0),   # 橫向 →
        (0, 1),   # 縱向 ↓
        (1, 1),   # 斜線 ↘
        (1, -1),  # 斜線 ↗
    ]

    for dx, dy in directions:
        count = 0  # 自己這一顆

        # 正方向
        nx, ny = x + dx, y + dy
        while (0 <= nx < BOARD_LINE_COUNT and
               0 <= ny < BOARD_LINE_COUNT and
               board[nx][ny] == player):
            count += 1
            nx += dx
            ny += dy

        # 反方向
        nx, ny = x - dx, y - dy
        while (0 <= nx < BOARD_LINE_COUNT and
               0 <= ny < BOARD_LINE_COUNT and
               board[nx][ny] == player):
            count += 1
            nx -= dx
            ny -= dy

        if count >= 4:
            return True

    return False

# pygame初始化
pg.init()
# 設定視窗
width, height = 640, 640
table = []
# 設定常數
BOARD_LINE_COUNT = 16
WIDTH_INT = width / (BOARD_LINE_COUNT + 1)
HIGHT_INT = height / (BOARD_LINE_COUNT + 1)
WIDTH_ENDPOINT = width - WIDTH_INT
HIGHT_ENDPOINT = height - HIGHT_INT
# 產生視窗
screen = pg.display.set_mode([width, height])
# 設定遊戲標題
pg.display.set_caption("五子棋")
# 建立畫布bg
bg = pg.Surface(screen.get_size())
# 把畫布填滿某個顏色
bg.fill([199, 167, 82])
# 開始畫棋盤
for i in range(0, BOARD_LINE_COUNT):
    y_axis = HIGHT_INT + i * HIGHT_INT
    pg.draw.line(bg, [50, 0, 50], [WIDTH_INT, y_axis], [WIDTH_ENDPOINT, y_axis], 2)

    x_axis = WIDTH_INT + i * WIDTH_INT
    pg.draw.line(bg, [0, 0, 0], [x_axis, HIGHT_INT], [x_axis, HIGHT_ENDPOINT], 2)

    a = []
    for j in range(0, BOARD_LINE_COUNT):
        a.append(0)
    table.append(a)

# 把某個圖層貼到上一層
screen.blit(bg, [0, 0])
# 對畫面進行更新(才會真的秀出來)
pg.display.update()

game_round = 0
sign = 0
running = True
while running:
    for event in pg.event.get():
    # 監聽所有 pygame 事件（滑鼠、鍵盤、視窗等）
    
        if event.type == pg.MOUSEBUTTONUP:
            # 當滑鼠按鍵「放開」時，視為一次落子行為
            
            x, y = pg.mouse.get_pos()
            # 取得滑鼠在視窗中的實際像素座標 (x, y)
            
            if game_round % 2 == 0:
                # 偶數回合：白子
                colors = [255, 255, 255]
                sign = 1
            else:
                # 奇數回合：黑子
                colors = [0, 0, 0]
                sign = -1

            # --- 以下是舊版用「距離線條」判斷最近交點的嘗試 ---
            # 保留作為思考紀錄，實際邏輯已改為 round()
            #
            # x_point = x // WIDTH_INT
            # y_point = y // HIGHT_INT
            # if (x % WIDTH_INT) <= (WIDTH_INT / 2):
            #     print('right_line')
            # else:
            #     x_point += 1
            #     print("leftline")
            # if (y % HIGHT_INT) <= (HIGHT_INT / 2):
            #     print('upper_line')
            # else:
            #     y_point += 1
            #     print("downline")

            # 將滑鼠像素座標轉換為棋盤格座標（取最近的交點）
            x_scale = round(x / WIDTH_INT)
            y_scale = round(y / HIGHT_INT)

            # 檢查：
            # 1. 是否在棋盤範圍內
            # 2. 該位置是否尚未落子
            if (1 <= x_scale <= BOARD_LINE_COUNT and
                1 <= y_scale <= BOARD_LINE_COUNT and
                table[x_scale - 1][y_scale - 1] == 0):

                # 將棋盤格座標轉回實際像素座標，用於畫棋子
                x_pos = x_scale * WIDTH_INT
                y_pos = y_scale * HIGHT_INT

                # 在棋盤背景上畫出棋子
                pg.draw.circle(
                    bg,
                    colors,
                    [x_pos, y_pos],
                    min(WIDTH_INT, HIGHT_INT) / 2 * 0.8,
                )

                # 更新棋盤資料（x 在前、y 在後）
                table[x_scale - 1][y_scale - 1] = sign

                # 將更新後的背景貼回螢幕
                screen.blit(bg, [0, 0])
                # 更新畫面顯示
                pg.display.update()

                # 判斷這一步是否形成五子連線
                if check_win(table, x_scale - 1, y_scale - 1):
                    running = False  # 結束遊戲

            else:
                # 若點擊到非法位置（超出棋盤或已有棋子）
                # 抵銷後面即將加上的回合數
                game_round -= 1

            # 回合數 +1（成功或失敗都會執行，失敗時已先 -1）
            game_round += 1


        # 如果收到的事件是按x
        if event.type == pg.QUIT:
            # 迴圈就會變成while False
            running = False
pg.quit()


     