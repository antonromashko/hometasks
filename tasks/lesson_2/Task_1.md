Создать функцию **monitor()**, которая принимает три аргумента - пути к каталогам.
Первый параметр - **каталог чтения**.
Второй - **каталог результатов**.
Третий - **каталог ошибок**.

Функция должна производить проверку каталога на наличие файлов **.txt*.
Найденые файлы должны содержать текстовое представление питоновского списка
целых чисел.
Функция должна вызывать функцию **process()**, которая принимает спископодобную строку,
преобразовывает в список и возвращает сумму его элементов.

Полученную сумму функция **monitor()** должна записать в одноименный файл в каталог результатов.

Исходный файл удаляется из каталога чтения.

Нюансы:
1. Если при обработке значения возникло любого рода исключение, исходный файлик с данными
   копируется в каталог ошибок.
2. Необходимо наличие файла main.py, в котором функция **monitor()** будет вызываться в бесконечном
   цикле с периодичностью **5 секунд**.
3. Содержимое входных файлов может быть любым. Но сумма должна посчитаться только для валидных.
   Пример валидного содержимого - строка "[1,2,3, 6, 4, 5]"
   
Бонусы:
1. Функцию **process()** необходимо обернуть в декоратор, который выведет при каждом запуске время выполнения
   и название переданной функции.
2. Придумать и задействовать функцию map() + lambda для процессинга файлов.
