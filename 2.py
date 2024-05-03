import turtle
import argparse

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Recursion level')
  parser.add_argument('recursion_level', nargs='?', help='Recursion level')
  args = parser.parse_args()
  print(args)
  recursion_level = args.recursion_level
  if recursion_level:
    recursion_level = int(recursion_level)
  else:
    print("Буде промальована сніжинка Коха.")
    recursion_level = int(input("Який ви бажаєте рівень рекурсії? "))

  draw_koch_curve(recursion_level)