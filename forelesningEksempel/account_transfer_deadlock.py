#coding=utf-8 
import time 
import threading 
class Account: 
  def __init__(self, _id, balance, lock): 
    self.id = _id 
    self.balance = balance 
    self.lock = lock 
 
  def withdraw(self, amount): 
    self.balance -= amount 
 
  def deposit(self, amount): 
    self.balance += amount 
 
def transfer(_from, to, amount): 
  _from.lock.acquire()# Lock your account  
  _from.withdraw(amount) 
  time.sleep(1) # Simulating the actual transaction
  print('Account ' + _from.id + ' waiting for lock for account ' + to.id + '\n') 
  to.lock.acquire()# Lock in each other's account  
  to.deposit(amount) 
  to.lock.release() 
  _from.lock.release() 
  print('Transfer finished succesfully!') 
 
a = Account('a',1000, threading.Lock()) 
b = Account('b',10000, threading.Lock()) 
#threading.Thread(target = transfer, args = [a, b, 100]).start()
#threading.Thread(target = transfer, args = [b, a, 200]).start() 
threading.Thread(target = transfer, args = (a, a, 500)).start() 
