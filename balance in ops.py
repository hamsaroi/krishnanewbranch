Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def make_account():
	return{'balance':0}

>>> def deposite(account,amount):
	account['balance']+=amount
	return account['balance']

>>> def withdraw(account,amount):
	account['balance']-=amount
	return account['balance']

>>> a=make_account()
>>> b=make_account()
>>> deposite(a,100)
100
>>> withdraw(b,10)
-10
>>> deposite(a,10)
110
>>> withdraw(b,1)
-11
>>> print("newchange")
