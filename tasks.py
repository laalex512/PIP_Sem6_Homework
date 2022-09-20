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
