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
window.geometry('450x600')

# DEFINING GUI ELEMENTS #1

logo = Label(window, text="$", fg="forest green", font=("Courier New", 60))
title = Label(window, text="Business Adam", fg="forest green", font=("Courier New", 20, "bold"))
undertitle = Label(window, text="Contractor Management System", fg="black", font=("Courier New", 8))
copyright = Label(window, text="©2020 Sankti", fg="grey", font=("Courier New", 8))

message_box = Text(window, width=60, height=32, wrap=WORD, fg="black", font=("Courier New", 8))
message_box.config(state=DISABLED)

request1 = Label(window, text="Please select an account number:", fg="black", font=("Courier New", 8))
acc_choice = StringVar()
acc_choice.set("001")

# DEFINING FUNCTIONS

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

def show_acc():
	acc_select = acc_choice.get()
	
	if acc_select == "001":
		write("\n" + "\n" +
		"Account no.:     " + str(Acc001.accno) + "\n" +
		"Name:            " + str(Acc001.accname) + "\n" +
		"Legal Entity:    " + str(Acc001.le) + "\n" +
		"Region:          " + str(Acc001.reg) + "\n" +
		"Country:         " + str(Acc001.cnt) + "\n" +
		"\n" +
		" - Master Sheet - " + "\n" +
		"Account status:  " + str(Acc001.accst) + "\n" +
		"LE status:       " + str(Acc001.lest) + "\n" +
		"\n" +
		" - Credit Control - " + "\n" +
		"Deposit value:   " + str(Acc001.depo) + "\n" +
		"Account Balance: " + str(Acc001.bal) + "\n" +
		"Overdue value:   " + str(Acc001.ovd))
		
	elif acc_select == "024":
		write("\n" + "\n" +
		"Account no.:     " + str(Acc024.accno) + "\n" +
		"Name:            " + str(Acc024.accname) + "\n" +
		"Legal Entity:    " + str(Acc024.le) + "\n" +
		"Region:          " + str(Acc024.reg) + "\n" +
		"Country:         " + str(Acc024.cnt) + "\n" +
		"\n" +
		" - Master Sheet - " + "\n" +
		"Account status:  " + str(Acc024.accst) + "\n" +
		"LE status:       " + str(Acc024.lest) + "\n" +
		"\n" +
		" - Credit Control - " + "\n" +
		"Deposit value:   " + str(Acc024.depo) + "\n" +
		"Account Balance: " + str(Acc024.bal) + "\n" +
		"Overdue value:   " + str(Acc024.ovd))

	elif acc_select == "070":
		write("\n" + "\n" +
		"Account no.:     " + str(Acc070.accno) + "\n" +
		"Name:            " + str(Acc070.accname) + "\n" +
		"Legal Entity:    " + str(Acc070.le) + "\n" +
		"Region:          " + str(Acc070.reg) + "\n" +
		"Country:         " + str(Acc070.cnt) + "\n" +
		"\n" +
		" - Master Sheet - " + "\n" +
		"Account status:  " + str(Acc070.accst) + "\n" +
		"LE status:       " + str(Acc070.lest) + "\n" +
		"\n" +
		" - Credit Control - " + "\n" +
		"Deposit value:   " + str(Acc070.depo) + "\n" +
		"Account Balance: " + str(Acc070.bal) + "\n" +
		"Overdue value:   " + str(Acc070.ovd))
	else:
		write("\n" + "\n" + "Error")
	
# DEFINING GUI ELEMENTS #2

dropdown_acc = OptionMenu(window, acc_choice, "001", "024", "070")
button_summon = Button(window, text="Show", font=("Courier New", 10, "bold"), command=lambda: show_acc())

# LAYOUT SETUP
	
logo.grid(row=0, rowspan=3, column=0)
title.grid(row=0, column=1, columnspan=6)
undertitle.grid(row=1, column=1, columnspan=6)
copyright.grid(row=2, column=1, columnspan=6)

request1.grid(row=3, column=0, columnspan=3, padx=10)
dropdown_acc.grid(row=3, column=3)
button_summon.grid(row=3, column=5, columnspan=3)

message_box.grid(row=5, rowspan=9, column=0, columnspan=7, padx=10)
write("Welcome to HeiFlow 2.0.")

# COMMENCING LOOP
 
window.mainloop()
