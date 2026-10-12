from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog
import os

root=Tk()
root.geometry("400x400")
root.config(bg="#ADC698")

file_name_entry = ' '
encryption_text_data = ' '
decryption_text_data = ' '

def saveData():
    global file_name_entry
    global encryption_text_data
    file_name_entry.get()