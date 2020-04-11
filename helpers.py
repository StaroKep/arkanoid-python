def create_end_game_text(canvas):
    return canvas.create_text(250, 120, text='Конец игры', font=('Courier', 30), fill='red')


def create_score_text(canvas, text, color):
    return canvas.create_text(475, 25, text=text, font=('Courier', 17), fill=color)