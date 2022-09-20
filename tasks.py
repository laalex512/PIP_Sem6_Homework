###################################################################################################

# 41. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:*
#         1+2*3 => 7;
#         (1+2)*3 => 9;


initStr = "16/ 2 +1-2* 3-5"
# Убираем лишние пробелы, если они есть:
initStr = initStr.replace(" ", "")
# Список, включающий строковое значение всех операций и операндов
elementList = []
beginCicle = 0
currentElement = ""
# Если строка начинается с отрицательного числа:
if initStr[0] == "-":
    currentElement = "-"
    beginCicle = 1
for i in range(beginCicle, len(initStr)):
    if initStr[i].isdigit():
        currentElement += initStr[i]
    else:
        elementList.append(currentElement)
        currentElement = ""
        elementList.append(initStr[i])
    if i == len(initStr)-1:
        elementList.append(currentElement)

print(elementList)

# Обрабатываем первые по приоритету операции * и /:
while "/" in elementList or "*" in elementList:
    for i in range(len(elementList)):
        if elementList[i] == "*":
            temp = int(elementList[i-1]) * int(elementList[i+1])
            elementList[i-1] = str(temp)
            elementList.remove(elementList[i])
            elementList.remove(elementList[i])
            print(elementList)
            break
        elif elementList[i] == "/":
            temp = int(int(elementList[i-1]) / int(elementList[i+1]))
            elementList[i-1] = str(temp)
            elementList.remove(elementList[i])
            elementList.remove(elementList[i])
            print(elementList)
            break

# Обрабатываем вторые по приоритету операции + и -:
while "+" in elementList or "-" in elementList:
    for i in range(len(elementList)):
        if elementList[i] == "+":
            temp = int(elementList[i-1]) + int(elementList[i+1])
            elementList[i-1] = str(temp)
            elementList.remove(elementList[i])
            elementList.remove(elementList[i])
            print(elementList)
            break
        elif elementList[i] == "-":
            temp = int(elementList[i-1]) - int(elementList[i+1])
            elementList[i-1] = str(temp)
            elementList.remove(elementList[i])
            elementList.remove(elementList[i])
            print(elementList)
            break

print(initStr + f" = {int(*elementList)}")


##############################################################################################

# Задача FOOTBALL: (необязательное) Напишите программу,
#  которая принимает на стандартный вход список
# игр футбольных команд с результатом матча и выводит на
# стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:

# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.

# Sample Input:
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


# def PrintDictionary(dict):
#     print("Club Name", end="\t")
#     for i in dict["Inter"].keys():
#         print(i, end="\t")
#     print()
#     for i in dict.keys():
#         print(i, end=":  \t")
#         for j in dict[i].keys():
#             print(dict[i][j], end="\t")
#         print()


# def GameProcessing(list, dictionary):
#     if list[1] > list[3]:
#         dictionary[list[0]]["Games"] += 1
#         dictionary[list[0]]["Wins"] += 1
#         dictionary[list[0]]["Points"] += 3
#         dictionary[list[2]]["Games"] += 1
#         dictionary[list[2]]["Looses"] += 1
#     elif list[1] < list[3]:
#         dictionary[list[2]]["Games"] += 1
#         dictionary[list[2]]["Wins"] += 1
#         dictionary[list[2]]["Points"] += 3
#         dictionary[list[0]]["Games"] += 1
#         dictionary[list[0]]["Looses"] += 1
#     else:
#         dictionary[list[0]]["Games"] += 1
#         dictionary[list[0]]["Draws"] += 1
#         dictionary[list[0]]["Points"] += 1
#         dictionary[list[2]]["Games"] += 1
#         dictionary[list[2]]["Draws"] += 1
#         dictionary[list[2]]["Points"] += 1


# dictTable = {
#     'Barcelona': {
#         "Games": 0,
#         "Wins": 0,
#         "Draws": 0,
#         "Looses": 0,
#         "Points": 0
#     },
#     'Victoria':  {
#         "Games": 0,
#         "Wins": 0,
#         "Draws": 0,
#         "Looses": 0,
#         "Points": 0
#     },
#     'Inter':  {
#         "Games": 0,
#         "Wins": 0,
#         "Draws": 0,
#         "Looses": 0,
#         "Points": 0
#     },
#     'Bavaria':  {
#         "Games": 0,
#         "Wins": 0,
#         "Draws": 0,
#         "Looses": 0,
#         "Points": 0
#     },
# }

# f = open("football.txt", "r")
# temp = f.read().replace("\n", ";").replace(" ", "").split(";")
# f.close()

# gameList = [[temp[i*4+j] for j in range(4)] for i in range(int(len(temp)/4))]

# for i in gameList:
#     GameProcessing(i, dictTable)

# print(gameList)
# PrintDictionary(dictTable)
