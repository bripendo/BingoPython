import tkinter as tk
import random
import urllib.request
import ctypes

# Constants for the grid
GRID_SIZE = 5
MIDDLE_INDEX = GRID_SIZE // 2

# insert data
def get_data():
    while True:
        try:
            print('1 - Użyj lokalnego pliku Dane.brip\n2 - Użyj pliku w chmurze')
            src = int(input())
            if src == 1:
                print('Otwieram plik...')
                with open('Dane.brip', 'r') as file:
                    data = [line.strip() for line in file.readlines() if line.strip()]
                return data
            elif src == 2:
                print('Łączę z serwerem Github...')
                url = 'https://raw.githubusercontent.com/bripendo/BingoPython/refs/heads/main/Dane.brip'
                response = urllib.request.urlopen(url)
                data = response.read().decode('utf-8').splitlines()
                return [line.strip() for line in data if line.strip()]
            else:
                print('Akceptowane wartości to: 1 lub 2')
        except ValueError:
            print('Wprowadź poprawną wartość: 1 lub 2.')

# minimalize console
def minimize_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 0)\

# clicking buttons
def bingo(r, c):
    current_color = buttons[(r, c)].cget("bg")
    new_color = "white" if current_color in ["lime", "brown"] else "brown"
    buttons[(r, c)].config(bg = new_color)
    check_win()

# green
def check_win():
    '''
    structure is
    if a row/column/diagonal if complete:
        switch color to lime
    else:
        switch lime back to brown
    '''
    for i in range(GRID_SIZE):
        # check rows
        if all(buttons[(i, j)].cget("bg") != "white" for j in range(GRID_SIZE)):
            for j in range(GRID_SIZE):
                buttons[(i, j)].config(bg = "lime")
        else:
            for j in range(GRID_SIZE):
                if buttons[(i, j)].cget("bg") == "lime":
                    buttons[(i, j)].config(bg = "brown")
    for i in range(GRID_SIZE):
        # check columns
        if all(buttons[(j, i)].cget("bg") != "white" for j in range(GRID_SIZE)):
            for j in range(GRID_SIZE):
                buttons[(j, i)].config(bg = "lime")
        else:
            for j in range(GRID_SIZE):
                if buttons[(j, i)].cget("bg") == "lime":
                    buttons[(j, i)].config(bg = "brown")
    # check diagonals
    if all(buttons[(i, i)].cget("bg") != "white" for i in range(GRID_SIZE)):
        for i in range(GRID_SIZE):
            buttons[(i, i)].config(bg="lime")
    if all(buttons[(i, GRID_SIZE - i - 1)].cget("bg") != "white" for i in range(GRID_SIZE)):
        for i in range(GRID_SIZE):
            buttons[(i, GRID_SIZE - i - 1)].config(bg = "lime")
# setup
def setup_bingo():
    data = get_data()
    name = data[0]
    random.shuffle(data)
    data[data.index(name)], data[12] = data[12], data[data.index(name)]  # middle workaround

    root = tk.Tk()
    root.title(name)

    # initialize
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            button = tk.Button(root, text = data[i * GRID_SIZE + j], bg = 'white',
                               command = lambda r = i, c = j: bingo(r, c), height = 5, width = 10, wraplength = 80)
            button.grid(row = i, column = j, padx = 5, pady = 5)
            buttons[(i, j)] = button
            root.grid_rowconfigure(i, weight = 1)
            root.grid_columnconfigure(j, weight = 1)

    # middle
    buttons[(MIDDLE_INDEX, MIDDLE_INDEX)].config(text='⭐', bg='brown', state='disabled')
    minimize_console()
    root.mainloop()

buttons = {}
setup_bingo()
