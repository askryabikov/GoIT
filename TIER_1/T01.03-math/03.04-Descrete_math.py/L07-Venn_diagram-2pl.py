# Почнемо з найпростішого випадку — дві множини. 
# Візьмемо приклад з користувачами веб-сайту, 
# які купували різні продукти.

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Користувачі, які купили продукт А і продукт Б
bought_A = {'user1', 'user2', 'user3', 'user5', 'user7'}
bought_B = {'user3', 'user4', 'user5', 'user6', 'user8'}

# Будуємо діаграму Венна
venn2([bought_A, bought_B], ('Продукт А', 'Продукт Б'))
plt.title('Покупці продуктів А і Б')
plt.show()


