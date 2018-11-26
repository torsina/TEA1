import csv


def describe():
    with open('titanic.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Les colonnes sont: {", ".join(row)}')
                line_count += 1
            else:
                print(f'{row}.')
                line_count += 1
        print(f'Il y avait {line_count - 1} passagers à bord du Titanic.')

def searchCount(column, wantedValue):
    with open('titanic.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        index_count = 0
        counter = 0
        dict = {}
        for row in csv_reader:
            if line_count == 0:
                for item in row:
                    dict[item] = index_count
                    index_count = index_count + 1

            line_count += 1
            if line_count != 0 and row[dict[column]] == wantedValue:
                counter = counter + 1

        print(counter)

def getColumn(column):
    with open('titanic.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        wantedIndex = 0
        result = []
        for row in csv_reader:
            if line_count == 0:
                for index, item in enumerate(row):
                    if item == column:
                        wantedIndex = index
                        break
            else:
                result.append(row[wantedIndex])
            line_count = line_count + 1
        return result

def average(column, type):
    column = getColumn(column)
    n = 0
    average = 0
    for item in column:
        if type == "number":
            if item == "":
                continue
            n = n + 1
            item = item.replace(",", ".")
            print(str(item))
            item = float(item)
            print(str(item))
            print(".")
            average = average + item
    average = average / n
    return average


def filterArray(column, value, input, dict = {}):
    with open('titanic.csv') as csv_file:
        database = csv.reader(csv_file, delimiter=',')
        if input:
            database = input
        line_count = 0
        index_count = 0
        result = []
        for row in database:
            if line_count == 0 and not bool(dict):
                for item in row:
                    dict[item] = index_count
                    index_count = index_count + 1

            line_count += 1
            if line_count != 0 and row[dict[column]] == value:
                result.append(row)
        return result

def getIndexDict():
    with open('titanic.csv') as csv_file:
        database = csv.reader(csv_file, delimiter=',')
        dict = {}
        for row in database:
            for index, item in enumerate(row):
                dict[item] = index
            break
        return dict


def filtersArray(list):
    dict = getIndexDict()
    with open('titanic.csv') as csv_file:
        database = csv.reader(csv_file, delimiter=',')
        for filter in list:
            database = filterArray(filter[0], filter[1], database, dict)
        return database

# print(filtersArray([["sex", "male"], ["age", "42"]])[0][2])

def maxPriceTicket():
    