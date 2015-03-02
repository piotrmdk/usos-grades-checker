from texttable import Texttable
import grades2


def tablemaker():
    table = Texttable()
    table.set_cols_align(["l", "c", "c"])
    table.set_cols_valign(["m", "m", "m"])
    table.set_cols_width([30, 8, 8])
    table.add_rows([["Nazwa", "Oceny 1", "Oceny 2"]])

    value = grades2.grades()

    for val in value:
        if type(val['unit']) is dict:
            unit_grades = ', '.join(val['unit'].values())
        else:
            unit_grades = ''
        table.add_rows([["Nazwa", "Oceny 1", "Oceny 2"], [val['name'].encode('utf-8'), unit_grades, val['grade']]])

    result = table.draw() + "\n"
    return result

