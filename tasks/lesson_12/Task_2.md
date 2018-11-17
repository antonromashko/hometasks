Написать регулярное выражение, позволяющее валидировать строку с адресом хоста и портом,
а также получать отдельно адрес хоста и порт.

Условия:

- хост может задаваться как IPv4 (т.е. вида 127.0.0.1, 10.22.254.1)
- IP-адрес хоста не может заканчиваться на 255 (четвертый блок адреса)
- диапазон значений для каждой части IP-адреса - от 0 до 255 включительно
- хост может задаваться как доменное имя (localhost, megusta.com, и т.п.)

Регулярка должна давать возможность выкусить отдельно адрес хоста и порт.

Пример:

localhost:5000 - groups содержит ('localhost','5000')
127.0.0.1:5000 - groups содержит ('127.0.0.1', '5000')
12.44.33.255:9800 - None, т.к. невалидный четвертый блок адреса


Дата выдачи: 17.11.2018