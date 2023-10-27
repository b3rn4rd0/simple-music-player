from tkinter import *
import pygame
from tkinter import filedialog
import os

root = Tk()
root.title('Caixa audio')

root.geometry("600x400")

pygame.mixer.init()  

mp3_files = [file for file in os.listdir() if file.endswith(".mp3")]
current_index = 0  

def stop():
    pygame.mixer.music.stop()

def choose_audio():
    global current_index
    initial_dir = os.path.dirname(__file__)  
    file_path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        play(file_path)
        mp3_files.append(file_path)  
        current_index = len(mp3_files) - 1  

def play(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(loops=0)

def play_next():
    global current_index
    if len(mp3_files) > 1:
        current_index = (current_index + 1) % len(mp3_files)
        play(mp3_files[current_index])

def play_previous():
    global current_index
    if len(mp3_files) > 1:
        current_index = (current_index - 1) % len(mp3_files)
        play(mp3_files[current_index])

title = Label(root, text="radio ", bd=9, relief=GROOVE,
              font=("times new roman", 50, "bold"), bg="white", fg="blue")
title.grid(row=0, column=0, columnspan=3, sticky="nsew")

play_button = Button(root, text="Toca Música", font=("Helvetica", 32), command=lambda: play(mp3_files[current_index]))
play_button.grid(row=1, column=1, pady=20)

previous_button = Button(root, font=("Helvetica", 20), command=play_previous, text="◄")
previous_button.grid(row=1, column=0, padx=10)

next_button = Button(root, font=("Helvetica", 20), command=play_next, text="►")
next_button.grid(row=1, column=2, padx=10)

stop_button = Button(root, text="Pare, por favor pare", font=("Helvetica", 20), command=stop)
stop_button.grid(row=2, column=1)

choose_button = Button(root, text="Escolha otra coisa", font=("Helvetica", 20), command=choose_audio)
choose_button.grid(row=3, column=1)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
