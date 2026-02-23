import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Визначаємо три множини чисел
more_than_10 = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
even = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
divisible_by_3 = {3, 6, 9, 12, 15, 18}

# Будуємо діаграму
venn3([more_than_10, even, divisible_by_3], ('>10', 'Парні', 'Кратні 3'))
plt.title('Властивості чисел від 2 до 20')
plt.show()
