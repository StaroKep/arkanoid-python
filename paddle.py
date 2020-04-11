import random

initial_speed = 0
position_over_bottom = 50
possible_starting_positions = [40, 60, 90, 120, 150, 180, 200]

right_arrow = '<KeyPress-Right>'
left_arrow = '<KeyPress-Left>'
return_button = '<KeyPress-Return>'

paddle_width = 100
paddle_height = 10


class Paddle:
    def __init__(self, canvas, color, speed):
        self.canvas = canvas

        # Рисуем прямоугольник и заполняем цветом
        self.id = canvas.create_rectangle(
            0, 0,
            paddle_width, paddle_height,
            fill=color
        )

        # Перемешиваем возможные стартовые позиции платформы
        random.shuffle(possible_starting_positions)
        # После перемешивания выбираем первый элемент массива
        self.starting_point_x = possible_starting_positions[0]
        # Можно было бы использовать random.choice или random.randint

        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        # Устанавливаем платформу в начальное положение
        self.canvas.move(
            self.id,
            self.starting_point_x,
            self.canvas_height - position_over_bottom
        )

        # Устанавливаем начальную скорость платформы
        self.x = initial_speed

        # Скорость платформы после начала игры
        # (после первого нажатия стрелок)
        self.speed = speed

        # Связываем зажатие кнопок с методами объекта
        self.canvas.bind_all(right_arrow, self.turn_right)
        self.canvas.bind_all(left_arrow, self.turn_left)
        self.canvas.bind_all(return_button, self.start_game)

        # Изначально игра не запущена
        self.started = False

    # При нажатии стрелки вправо
    def turn_right(self, event):
        # x - скорость изменения координаты x
        self.x = self.speed

    # При нажатии стрелки влево
    def turn_left(self, event):
        # Скорость изменения координаты x станет отрицательной
        # Т.к. надо перемещаться в противоположную сторону
        self.x = -self.speed

    # При нажатии кнопки Enter (Return) запустится игра
    def start_game(self, event):
        self.started = True

    # Перемещаем платформу в зависимости от текущей скорости
    def draw(self):
        # Перемещаем платформу по горизонтали
        self.canvas.move(self.id, self.x, 0)

        # Получаем координаты платформы
        pos = self.canvas.coords(self.id)

        # Ограничиваем ее перемещение стенками холста
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
