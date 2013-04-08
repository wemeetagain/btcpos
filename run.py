#!/usr/bin/python
import btcpos
import threading
import Queue

identifier=''
forwardingaddress=''
password=''
#eg: identifier='6ne3m2m7-6534-2k6l-2h1b-59v2xm0g8yio'
#    password='mypassword'
#    forwardingaddress='17yHkgQooxxMdB7iqNbBXDrV8YdMrMes5d'

p= btcpos.POS(identifier,password,forwardingaddress)
t= threading.Thread(target=p.transactionLoop)
t.start()
p.gui.mainloop()
