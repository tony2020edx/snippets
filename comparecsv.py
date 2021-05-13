
import csv


verify_list = []

master_list = []


def process_verify():

    filename = open('output.csv', 'r')

    file = csv.DictReader(filename, delimiter=';')

    for col in file:

        verify_list.append(col['Product_url'])

        #print(col['Product_url'])


process_verify()

print(len(verify_list))

def master_data():

    filename = open('verofy3.csv', 'r')

    file = csv.DictReader(filename, delimiter=';')

    for col in file:

        master_list.append(col['Product_url'])

        #print(col['Product_url'])

master_data()

print(len(master_list))

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

print(Diff(master_list, verify_list))

