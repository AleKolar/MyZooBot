Здравствуйте! Это концепт-бота опросника, который по одному ему известной логике(что очень заманчиво!) выдает результат пользователю. Пытаясь выяснить, как всё устроено
Пользователь получает ответ, что вот Ваш результат и с этим ничего не сделать, а пытаясь поговорить с ним, "Он" такой: Я здесь не для светских бесед, а чтоб определить Ваше..."
В общем нужна была настоящая клиент-сервисная БД, и я ,уже начал делать на Postgresql(файл в Code), надо отметить Redis и Mongo, пока отказались работать на моей машине. 
Думаю дай подключу, пока Docker desktop, ну понятно не пошел "он" сразу. Все делал по науке: wsl2, работа на терминале из под ubuntu, виртуализировал все, что мог. Но образ собрал.
Ставлю linax как вторую ОС. Все затормозило, зафризило. Думаю сгублю машину не дойду до финального проекта. Postgresql при выборе сервера пошел в бесконечную загрузку.
В общем одумался подключил SQlite3 - понятно не маштабируема, но для учебных целей оч.хорошо(все как Postgresql, только без возможности подсоединения). 
Данный aiogram Бот прямолинеен. Как только нашел, способ исполнить задуманное отбросил все лишнее для надежности. Так как маштабируемости надо добиваться залил его на Repl.it https://replit.com/@alekolar17982/Python 
(обязательно сходите на Repl.it: Repl.it https://replit.com/@alekolar17982/Python), теперь его можно build output на Heroku и в Twitter - это опять же маштабируемость! 
Да, и flask его "Будит"!. Концепт, вообще - Удачный к нему че хош прикрутить можно, конечно стрструктура не вот Latand - ботостроение, ну не все по solid. Но в целом 
устойчивая и надежная структура! Да и в getenv не стал прятать token - для удобства, но он(метод) "закоммитеный".
