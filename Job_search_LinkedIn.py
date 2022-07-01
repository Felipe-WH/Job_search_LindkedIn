from bs4 import BeautifulSoup
from requests import *
from tkinter import *
import webbrowser

window = Tk()
window.geometry("400x450")

L1 = Label(window, text="Digite o cargo").pack(anchor= W)
cargo = Entry(window)
cargo.pack(anchor=W)

L1 = Label(window, text="Digite o local").pack(anchor=W)
local = Entry(window)
local.pack(anchor=W)

def formatar_cargo():
    cargo2 = str(cargo.get()).replace(" ","%20")
    local2 = str(local.get()).replace(" ","%20")

    url = f'https://br.linkedin.com/jobs/search?keywords={cargo2}&location={local2}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    html = get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    vagas1 = soup.findAll("a",href=True)
    vagas= []
    x=-3
    for a in vagas1:
        x+=1
        vagas.append(a["href"])   
    exibir = vagas[4:14]
    listbox(exibir)

button = Button(window,text="enviar", command = formatar_cargo)
button.pack(anchor = W, pady= 15)

def callback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        url = event.widget.get(index)
    google(url)
    

def listbox(exibir):
    listbox = Listbox(window)
    listbox.pack(side="top", fill="both", expand=True)
    listbox.bind("<<ListboxSelect>>", callback)
    
    for i in exibir:
        listbox.insert("end",i)
        
label = Label(window).pack(side="bottom", fill="x")        
        
def google(url):
    webbrowser.open(url)
    
window.mainloop()
