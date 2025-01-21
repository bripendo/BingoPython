import tkinter as tk
import random
import urllib.request
import ctypes

print('1 - Użyj lokalnego pliku Dane.brip\n'
      '2 - Użyj pliku w chmurze')

a=[]

buttons={}



def DataInput():
    global a
    src = 2
    try:
        src = int(input())
    except ValueError:
        print('Akceptowane wartości to:\n'
              '1 - Użyj lokalnego pliku Dane.brip\n'
              '2 - Użyj pliku w chmurze')
        DataInput()
    finally:
        if src == 1:
            print('Otwieram plik...')
            with open('Dane.brip', 'r') as file:
                a = file.readlines()
                [line.strip() for line in a]
                if '' in a:
                    a.remove('')
        elif src == 2:
            print('Łączę z serwerem Github...')
            url = 'https://raw.githubusercontent.com/bripendo/BingoPython/refs/heads/main/Dane.brip'
            response = urllib.request.urlopen(url)
            data = response.read().decode('utf-8')
            a = data.split('\n')
            [line.strip() for line in a]
            if '' in a:
                a.remove('')
        else:
            print('Akceptowane wartości to:\n'
                  '1 - Użyj lokalnego pliku Dane.brip\n'
                  '2 - Użyj pliku w chmurze')
            DataInput()

        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(hwnd, 0) #minimalizuj konsolę

DataInput()

name=a[0]
random.shuffle(a)
a[a.index(name)],a[12]=a[12],a[a.index(name)] # jestem leniwy i nazwa bingo idzie jako zapychacz pod gwiazdkę

root = tk.Tk()
root.title(name)

 #specjalna lista na przechowywanie przyciskow

# przyciski są toggleable
def bingo(r, c):
    current_color = buttons[(r,c)].cget("bg")
    new_color = "brown" if current_color == "white" else "white"
    buttons[(r, c)].config(bg=new_color)
# siatka 5x5
for i in range(5):
    for j in range(5):
        button = tk.Button(root, text=a[i*5+j], bg='white', command=lambda r=i, c=j: bingo(r, c),height=5,width=10,wraplength=80)
        button.grid(row=i, column=j, padx=5, pady=5,)
        buttons[(i, j)] = button
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(j,weight=1)

buttons[(2,2)].config(text='⭐',bg='brown',state='disabled') #srodek
root.mainloop()
