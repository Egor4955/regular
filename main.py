import re
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    my_list = []


def phone():
    pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    subst_pattern = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = pattern.sub(subst_pattern, column[5])
    return


def names():
    pattern = r'([А-Я])'
    subst_pattern = r' \1'
    for column in contacts_list[1:]:
        x = re.sub(pattern, subst_pattern, (column[0] + column[1] + column[2])).split()
        if len(x) == 3:
            column[0] = x[0]
            column[1] = x[1]
            column[2] = x[2]
        elif len(x) == 2:
            column[0] = x[0]
            column[1] = x[1]
            column[2] = ''
        elif len(x) == 1:
            column[0] = x[0]
            column[1] = ''
            column[2] = ''
    return


def duplicates():
    for column in contacts_list[1:]:
        firstname = column[0]
        lastname = column[1]
        for el in contacts_list:
            new_firstname = el[0]
            new_lastname = el[1]
            if firstname == new_firstname and lastname == new_lastname:
                if column[2] == '':
                    column[2] = el[2]
                if column[3] == '':
                    column[3] = el[3]
                if column[4] == '':
                    column[4] = el[4]
                if column[5] == '':
                    column[5] = el[5]
                if column[6] == '':
                    column[6] = el[6]

    for contact in contacts_list:
        el = contact[0:7]
        if el not in my_list:
            my_list.append(contact)
    return my_list


if __name__ == '__main__':
    phone()
    names()
    duplicates()

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(my_list)