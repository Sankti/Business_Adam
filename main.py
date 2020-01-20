from tkinter import *

# DEFINING CLASS & CREATING DATABASE

class Account:
  def __init__(self, accno):
    self.accno = accno
    self.accname = []
    self.le = []
    self.reg = []
    self.cnt = []
    self.accst = []
    self.lest = []
    self.depo = []
    self.bal = []
    self.ovd = []

  def add_name(self, accname):
    self.accname.append(accname)

  def add_le(self, le):
    self.le.append(le)

  def add_reg(self, reg):
    self.reg.append(reg)

  def add_cnt(self, cnt):
    self.cnt.append(cnt)

  def add_accst(self, accst):
    self.accst.append(accst)

  def add_lest(self, lest):
    self.lest.append(lest)

  def add_depo(self, depo):
    self.depo.append(depo)

  def add_bal(self, bal):
    self.bal.append(bal)

  def add_ovd(self, ovd):
    self.ovd.append(ovd)

Acc001 = Account("001")
Acc001.add_name("Thundermass Trade Account")
Acc001.add_le("Thundermass Ltd")
Acc001.add_reg("Upper Silesia")
Acc001.add_cnt("Poland")
Acc001.add_accst("Active")
Acc001.add_lest("Active")
Acc001.add_depo(float(10000))
Acc001.add_bal(float(241520.20))
Acc001.add_ovd(float(12004.20))

Acc024 = Account("024")
Acc024.add_name("Glitterstick Fenoarivobe")
Acc024.add_le("Andrianampoinimerina GmbH")
Acc024.add_reg("Bongolava")
Acc024.add_cnt("Madagascar")
Acc024.add_accst("Inactive")
Acc024.add_lest("Dissolved")
Acc024.add_depo(float(0))
Acc024.add_bal(float(600.00))
Acc024.add_ovd(float(600.00))

Acc070 = Account("070")
Acc070.add_name("Polski Pub w Chitre")
Acc070.add_le("El Gringo Ltd")
Acc070.add_reg("Herrera")
Acc070.add_cnt("Panama")
Acc070.add_accst("Inactive")
Acc070.add_lest("Liquidated")
Acc070.add_depo(float(1000))
Acc070.add_bal(float(-1620.00))
Acc070.add_ovd(float(-1620.00))

# TKINTER GUI SETUP

window = Tk()
window.title("Business Adam")
window.geometry('800x600')

# DEFINING GUI ELEMENTS

logo = Label(window, text="$", fg="forest green", font=("Courier New", 60))
title = Label(window, text="Business Adam", fg="forest green", font=("Courier New", 20, "bold"))
undertitle = Label(window, text="Contractor Management System", fg="black", font=("Courier New", 8))
copyright = Label(window, text="©2020 Sankti", fg="grey", font=("Courier New", 8))

message_box = Text(window, width=40, height=24, wrap=WORD, fg="black", font=("Courier New", 10))
message_box.config(state=DISABLED)

request1 = Label(window, text="Please select an account number:", fg="black", font=("Courier New", 8))
button_summon = Button(window, text="Show", font=("Courier New", 10, "bold"))

row_name0 = Label(window, text="Account", fg="black", font=("Courier New", 8))
row_name1 = Label(window, text="Name", fg="black", font=("Courier New", 8))
row_name2 = Label(window, text="Legal Entity", fg="black", font=("Courier New", 8))
row_name3 = Label(window, text="Region", fg="black", font=("Courier New", 8))
row_name4 = Label(window, text="Country", fg="black", font=("Courier New", 8))

row_name5 = Label(window, text="Acc Status", fg="black", font=("Courier New", 8))
row_name6 = Label(window, text="LE Status", fg="black", font=("Courier New", 8))
row_name7 = Label(window, text="Deposit", fg="black", font=("Courier New", 8))
row_name8 = Label(window, text="Balance", fg="black", font=("Courier New", 8))
row_name9 = Label(window, text="Overdue", fg="black", font=("Courier New", 8))

# DEFINING FUNCTIONS

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

# LAYOUT SETUP
	
logo.grid(row=0, rowspan=3, column=0)
title.grid(row=0, column=1, columnspan=6)
undertitle.grid(row=1, column=1, columnspan=6)
copyright.grid(row=2, column=1, columnspan=6)

request1.grid(row=3, column=1, columnspan=3)
button_summon.grid(row=3, column=5, columnspan=3)

row_name0.grid(row=4, column=0)
row_name1.grid(row=5, column=0)
row_name2.grid(row=6, column=0)
row_name3.grid(row=7, column=0)
row_name4.grid(row=8, column=0)

row_name5.grid(row=4, column=2)
row_name6.grid(row=5, column=2)
row_name7.grid(row=6, column=2)
row_name8.grid(row=7, column=2)
row_name9.grid(row=8, column=2)

message_box.grid(row=5, rowspan=5, column=5, columnspan=3, pady=20)
write("Welcome to HeiFlow 2.0.")
 
window.mainloop()