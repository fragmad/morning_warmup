#!/usr/bin/env python3

# Write a program that prints a multiplication table for numbers up to 12.

def create_table(row, max_table):
    table_list = []
    for n in range(1, max_table + 1):
        table_list.append(row * n)

    return table_list

def create_tables(max_table):
    tables = []
    for n in range(1, max_table + 1):
        new_table = create_table(n, max_table)
        tables.append(new_table)
       
    return tables

def stdout_tables(tables):
    for r in tables:
        stdout_row = ""
        for n in r:
            stdout_row = stdout_row + (f" {n:03} |")
        print(stdout_row)

if __name__ == '__main__':
    tables = create_tables(12)
    stdout_tables(tables)
