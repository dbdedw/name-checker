import  os, time, ctypes, datetime, os.path, tkinter
from requests_html import HTMLSession
from tkinter import filedialog
e = datetime.datetime.now()
root = tkinter.Tk()
root.withdraw()

session = HTMLSession()

global emails
emails = []

if not os.path.exists("./input.txt"):
    f= open("input.txt","w+")
if not os.path.exists("results"):
    os.makedirs("results/")
if not os.path.exists("results/untaken"):
    os.makedirs("results/untaken")
if not os.path.exists("results/taken"):
    os.makedirs("results/taken")

def load_combos():
    global emails
    print()
    input("  Press ENTER to select combos..")
    fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameCombo is None:
        print()
        print("  Please select valid combo file..")
        time.sleep(2)
    else:
        try:
            with open(fileNameCombo.name, 'r+', encoding='utf-8') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        email = line.split()[0].replace('\n', '')
                        emails.append(email)
                    except:
                        pass
            print("  Loaded [{}] combos lines..".format(len(email)))
            time.sleep(2)
        except Exception:
            print("  Your combo file is probably harmed, please try again..")
            time.sleep(2)

username = emails
session = HTMLSession()

r = session.get(f"https://fortnitetracker.com/profile/search?q={username}")
if r.html.search('404 Not Found'):
  print(f"Name: '{username}' is available!")
  open('results/untaken/untaken.txt', 'a+').write("{}\n".format(username))

if r.html.search('Overview'):
  open('results/taken/taken.txt', 'a+').write("{}\n".format(username))
