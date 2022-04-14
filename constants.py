# этот файл для глобальных констант. чтобы не хардкодить строки/числа в коде, выносите их сюда.
# например вместо C:\\Windows в коде, создайте константу WINDOWS_PATH здесь и присвойте ей значение

# Пример

# CONSTANT_NAME = "value"
# LOG_DIR = "logs"


import os.path


DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'data/movies.db')
