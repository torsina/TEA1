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

def getColumn(column, database):
    with open('titanic.csv') as csv_file:
        if not database:
            database = csv.reader(csv_file, delimiter=',')
        dict = getIndexDict()
        wantedIndex = 0
        result = []
        for index, row in enumerate(database):
            if index == 0 and dict:
                wantedIndex = dict[column]
            else:
                result.append(row[wantedIndex])
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
            item = float(item)
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
    column = getColumn("fare")
    max = 0
    for item in column:
        if item == "":
            continue
        item = item.replace(",", ".")
        if float(item) > max:
            max = float(item)
    max = str(max).replace(".", ",")
    array = filtersArray([["fare", max]])
    return array

# print(len(maxPriceTicket()))

def survivors(sex):
    allSex = filtersArray([["sex", sex]])
    filteredSex = filtersArray([["sex", sex], ["survived", "1"]])
    return len(filteredSex)/len(allSex)

def womenFirst():
    women = survivors("female")
    men = survivors("male")
    print(str(round(women * 100, ndigits=0)), str(round(men * 100, ndigits=0)))
