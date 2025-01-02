import tkinter as tk
import random
import urllib.request
url = 'https://raw.githubusercontent.com/bripendo/BingoPython/refs/heads/main/Dane.brip'
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

a = data.split('\n')
a = [line.strip() for line in a]
name=a[0]
random.shuffle(a)
a[a.index(name)],a[12]=a[12],a[a.index(name)] # jestem leniwy i nazwa bingo idzie jako zapychacz pod gwiazdkę

root = tk.Tk()
root.title(name)

buttons={} #specjalna lista na przechowywanie przyciskow

# przyciski są toggleable
def bingo(r, c):
    current_color = buttons[(r,c)].cget("bg")
    new_color = "brown" if current_color == "white" else "white"
    buttons[(r,c)].config(bg=new_color)

# siatka 5x5
for i in range(5):
    for j in range(5):
        button = tk.Button(root, text=a[i*5+j], bg='white', command=lambda r=i, c=j: bingo(r, c),height=5,width=10,wraplength=80)
        button.grid(row=i, column=j, padx=5, pady=5,)
        buttons[(i, j)] = button
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(j,weight=1)

'''
def aspect_ratio(event):
    desired_aspect_ratio = 16 / 9  # Example aspect ratio (width / height)

    # Calculate the new dimensions while maintaining the aspect ratio
    new_width = event.width
    new_height = int(new_width / desired_aspect_ratio)

    # Update the window size
    if new_height != event.height:
        root.geometry(f"{new_width}x{new_height}")
        root.update_idletasks()


root.bind("<Configure>", aspect_ratio)
'''
buttons[(2,2)].config(text='⭐',bg='brown',state='disabled') #srodek
root.mainloop()
