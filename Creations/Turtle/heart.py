import turtle

def draw_heart():
    # Configuração da tartaruga
    t = turtle.Turtle()
    t.speed(2)
    t.color('red')
    t.begin_fill()

    # Desenha o coração
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    
    # Escreve a mensagem no meio do coração
    t.penup()
    t.goto(0, 150)  # Ajusta a posição do texto
    t.color('black')
    t.write("I Love You", align="center", font=("Arial", 30, "bold"))  # Ajusta o tamanho da fonte
    t.hideturtle()

# Configuração da tela
screen = turtle.Screen()
screen.title("Heart Drawing")
screen.bgcolor("white")

draw_heart()

# Mantém a janela aberta até que seja fechada pelo usuário
screen.mainloop()
