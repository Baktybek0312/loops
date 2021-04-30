# 4. Напишите код, который выведет на экран список языков с нумерацией.
#
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#
# Вывод:
#
#  0 go
#
#  1 java
#
#  2 php
#
#  3 python
#
#  4 javascript
#
#  5 ruby
#
# 5. Напишите цикл который выведет на экран:     1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
#
# Усиление:
#
# Получите такой же результат но с ОДНИМ циклом

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for i in range(6):
    print(i, languages[i])
