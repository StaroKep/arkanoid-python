from helpers import create_score_text

initial_score = 0

class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas

        # Устанавливаем начальное количество очков
        self.score = initial_score

        # Отображаем начальный счет на холсте
        self.id = create_score_text(canvas, self.score, color)

    # При вызове этого метода счет увеличится на 1
    # И элемент холста обновится с новым значением
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)