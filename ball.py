import random
from helpers import create_end_game_text

ball_size = 15
initial_x_position = 250
initial_y_position = 100

# Здесь:
# self.x - скорость изменения координаты x
# self.y - скорость изменения координаты y


class Ball:
    def __init__(self, canvas, paddle, score, color, speed):
        # Т.к. шарик взаимодействует с другими объектами и влияет на них
        # Связываем его с этоими оюъектами
        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        # Устанавливаем скорость шарика
        self.speed = speed

        # Рисуем щарик на холсте и запоминаем его уникальный идентификатор
        self.id = canvas.create_oval(0, 0, ball_size, ball_size, fill=color)

        # Устанавливаем шарик в начальное положение
        self.canvas.move(self.id, initial_x_position, initial_y_position)

        # Список возможных начальных скоростей шарика по оси x
        possible_initial_x_speed = [-self.speed, self.speed]
        # Перемешиваем этот список, чтобы получить
        # случайной начальное направление движения
        random.shuffle(possible_initial_x_speed)
        # Выбираем первый элемент перемешенного списка
        self.x = possible_initial_x_speed[0]

        # Изначально шарик летит вверх
        self.y = -self.speed

        # Запоминаем выосту и ширину холста
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        # Изначально шарик не сталкивался с дном
        self.hit_bottom = False

    # Описываем перемещение шарика
    def draw(self):
        # Перемещаем шарик по текущим по текщим скоростям
        # изменения координат x и y
        self.canvas.move(self.id, self.x, self.y)
        # Запоминаем новое положение щарика
        pos = self.canvas.coords(self.id)

        # Если шарик вышел за пределы холста сверху
        if pos[1] <= 0:
            # Меняем его скорость по оси y, чтобы он начал падать
            self.y = self.speed

        # Если шарик вышел за пределены холста снизу (столкнулся с дном)
        if pos[3] >= self.canvas_height:
            # Запоминаем это в специальное свойство
            self.hit_bottom = True
            # Выводим сообщение о завершении игры
            create_end_game_text(self.canvas)

        # Если шарик ударился о платформу
        if self.hit_paddle(pos):
            # Меняем его скорость по оси y, чтобы он начал лететь вверх
            self.y = -self.speed

        # Если шарик вышел за пределены холста слева
        if pos[0] <= 0:
            # Направляем его вправо
            self.x = self.speed

        # Если шарик вышел за пределены холста справа
        if pos[2] >= self.canvas_width:
            # Направляем его влево
            self.x = -self.speed

    # Проверяем пересекается ли шарик с платформой
    def hit_paddle(self, pos):
        # Получаем координаты платформы
        paddle_pos = self.canvas.coords(self.paddle.id)

        # Если шарик пересекся с платформой
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()  # Увеличиваем счет
                return True  # Сообщаем наружу, что да, шарик столкнулся с платформой

        return False