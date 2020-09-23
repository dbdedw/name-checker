import requests
from requests_html import HTMLSession
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
from colorama import Fore, init
from re import search
import datetime
from tkinter import filedialog, messagebox
e = datetime.datetime.now()

current_date = e.strftime("%Y-%m-%d-%H-%M-%S")
session = HTMLSession()
root = tkinter.Tk()
root.withdraw()

if not os.path.exists("results"):
    os.makedirs("results/")
if not os.path.exists('results/untaken'):
    os.makedirs('results/untaken')
if not os.path.exists('results/taken'):
    os.makedirs('results/taken')
if not os.path.exists('results/untaken/{}'.format(current_date)):
    os.makedirs('results/untaken/{}'.format(current_date))
if not os.path.exists('results/taken/{}'.format(current_date)):
    os.makedirs('results/taken/{}'.format(current_date))

username = input("Fortnite Name: ")
session = HTMLSession()

r = session.get(f"https://fortnitetracker.com/profile/search?q={username}")
if r.html.search('404 Not Found'):
  print(f"Name: '{username}' is available!")
  open('results/untaken/{}/untaken.txt'.format(current_date), 'a+').write("{}".format(username))

if r.html.search('Overview'):
  open('results/taken/{}/taken.txt'.format(current_date), 'a+').write("{}".format(username))
