import sys
import os
print('123')
if sys.prefix == sys.base_prefix:
    print('Вы не активировали виртуальное окружение')
    print(f'Текущее окружение {sys.base_prefix}')
    os.system("pip list")
else:
    print(f'Вы используете виртуальное окружение {sys.prefix}')
    os.system("pip list")