# Основні кольори у RGB-просторі (значення від 0 до 255)
import numpy as np
red = np.array([255, 0, 0])
green = np.array([0, 255, 0])
blue = np.array([0, 0, 255])

print("Основні кольори:")
print(f"  Червоний: {red}")
print(f"  Зелений:  {green}")
print(f"  Синій:    {blue}")

# Отримуємо нові кольори через лінійні комбінації
olive = 0.5*red + 0.5*green + 0*blue
purple = 0.5*red + 0*green + 0.5*blue
cyan = 0*red + 0.5*green + 0.5*blue
white = 0.33*red + 0.33*green + 0.33*blue

print("Нові кольори (лінійні комбінації):")
print(f"  Оливковий:     {olive.astype(int)} = 0.5×red + 0.5×green")
print(f"  Пурпуровий: {purple.astype(int)} = 0.5×red + 0.5×blue")
print(f"  Темно-бірюзовий:  {cyan.astype(int)} = 0.5×green + 0.5×blue")
print(f"  Темно-сірий:      {white.astype(int)} = 0.33×red + 0.33×green + 0.33×blue")



# Основні кольори:
#   Червоний: [255   0   0]
#   Зелений:  [  0 255   0]
#   Синій:    [  0   0 255]

# Нові кольори (лінійні комбінації):
#   Оливковий:     [127 127   0] = 0.5×red + 0.5×green
#   Пурпуровий: [127   0 127] = 0.5×red + 0.5×blue
#   Темно-бірюзовий:  [  0 127 127] = 0.5×green + 0.5×blue
#   Темно-сірий:      [84 84 84] = 0.33×red + 0.33×green + 0.33×blue