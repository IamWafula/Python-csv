import csv
from numpy.lib.shape_base import column_stack
import numpy as np


def start():
    print("1 - Attendance Stats \n")
    print("2 - Revenue Stats \n")
    print("3 - Perfomance Stats \n")

def valid_stat():
    cont = True
    while cont:
        try:
            stat = int(input("Please select an option (0 to exit):"))
            if stat<=3 and stat>0:
                cont = False
            elif stat==0:
                exit()   
            else:
                print("Invalid option. Try again: ")
        except Exception as e:
            print(e)
    return stat

def stat_func(num):
    if num==1:
        return 7
    elif num == 2:
        return 9
    elif num == 3:
        return 11



def mon_totals(final):
    month = 1  
    while month < 12:
        for f in final:
            t_month = 0
            if f == month:
                t_month = t_month + final[1]


def row1(month):
    column = "|    |"
    column = list(column)

    month = str(month)
    month = list(month)

    column_slice1 = column[0:4]
    column_slice2 = column[4:len(month)]
    column_slice3 = column[len(month):]
    column_slice2 = month

    column = np.concatenate((column_slice1,column_slice2, column_slice3))
    col = ''.join(map(str,column))

    return col



def row2(data):
    month = 1
    data = data[1:13]
    for i in data:
        column = "             |"
        column = list(column)

        i = str(i)
        i = list(i)

        column_slice1 = column[0:5]
        column_slice2 = column[5:len(i)]
        column_slice3 = column[len(i):]
        column_slice2 = i

        column = np.concatenate((column_slice1,column_slice2, column_slice3))
        col = ''.join(map(str,column))

        row = row1(month)
        print(row + col)
        month = month + 1

def header():
    print("----------------------------")
    print("|  Month |      Total       |")
    print("-----------------------------")


def print_f(out, term, movie, yr):
    if term==1:
        term = "Attendance stats"
    elif term == 2:
        term = "Revenue Stats"
    elif term == 3:
        term = "Perfomance Stats"

    index, mth = 0, 1
    total = 0

    while mth <= 12:
        mth = mth + 1
        index = index + 1
        total = total + int(out[index])
    if total > 0:
        print("Term: " + movie + "\n" + "Year: " + str(yr) + "\n" + "Stat: " + term + "\n")
        header()
        row2(out)
        print("-----------------------------")
        print("Total        " + str(total) + "\n")
    else:
        print("No Data Found.")

def main():
    
    with open('broadway.csv') as file:
        months = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        start()
        stat = int(valid_stat())
        name = input("Enter search name:")
        year = int(input("Enter year: "))
        data = stat_func(stat)
        print("\n")
        shows = csv.reader(file)
        next(shows)
        for show in shows:
            if int(show[3]) == year:
                m_name = show[4].lower()
                if m_name.find(name.lower(), 0) > -1:
                    final_dat = [show[2], show[data]]    
                    months[int(final_dat[0])] = months[int(final_dat[0])] + int(final_dat[1])
    print_f(months,stat,name,year)
                    
    

if __name__ == '__main__':
    main()