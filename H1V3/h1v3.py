import os, time, sys, socket
try:
	import colorama
	from colorama import Fore, Back, Style
	colorama.init(autoreset=True)
except:
	print " Please Install Colorama To Continue ... 'pip install colorama'"
	sys.exit(1)
	
# Memory Class 
class Memory:
	Cns 	= Console()
	Memory = {
		'setting:index':[ 'temp', 'mount@start' ], # setting index
		'setting.temp':'', # template setting
		'setting.mount@start':False, # mount plufins at start
		'display:index':[ 'templates', 'messages' ] ,# display index
		'display.templates:index':[ 'basic' ] ,# basic template
		'display.templates:rules':'EXIST WARN+NORM+CRIT+BANN+INPUT' ,# rules must me inside string +
		'display.templates.basic.WARN':Fore.RED+Style.BRIGHT+' [ WARNING ] '+Fore.GREEN+' <<:?:>> ', 
		'display.templates.basic.NORM':Fore.GREEN+Style.BRIGHT+' [ NORMAL ] '+Fore.WHITE+' <<:?:>> ',
		'display.templates.basic.CRIT':Fore.RED+Style.BRIGHT+' [ CRITICAL ] '+Fore.GREEN+' <<:?:>> ',
		'display.templates.basic.BANN':"",
		'display.templates.basic.INPUT':Fore.GREEN+' ['+str(socket.gethostname())+'] '+Fore.YELLOw+'    ?:>>',
		'input:index':[ 'FILTER' ] ,
		'input.FILTER:index':[ 'h1v3' ],
		'input.Filter.h1v3:index':[]
		
	} 		# Main Memory Object 
	
	# Memory Handler 
	def MemoryHandler(self, LOC=None, ACT=None, VAR=None, OVR=False):
		# Check Actions
		if ACT == None:
			self.Cns.Display(head='WARN', msg=' No Action Entered...')
			return None
			
		else:
			# Append Action
			if ACT in [ 'append', 'Append' ]:
				if LOC in self.Memory:
					if OVR == False:
						self.Cns.Display(head='WARN', msg=' Overide Failed')
						return None
					else:
						pass
					
					pass
					
				self.Memory[str(LOC)] = VAR
				return None
				
			# Remove Action
			elif ACT in [ 'remove', 'Remove' ]:
				if LOC in self.Memory:
					if OVR == False:
						self.Cns.Display(head='WARN', msg=' Failed Overide Not allowed')
						return None
					del(self.Memory[str(LOC)])
					return None
				else:
					self.Cns.Display(head='WARN', msg=' Memory Entity '+str(LOC)+' Does not Exist')
					return None
					
			# Status Action
			elif ACT in [ 'status', 'Status' ]:
				if LOC in self.Memory:
					status = self.Memory[str(LOC)]
					return status
				else:
					self.Cns.Display(head='WARN', msg=' Memory Entity '+str(LOC)+' Does not Exists')
					return None
				
			else:
				self.Cns.Display(head='WARN', ' Action Does Not Exist')
				return None
				
		
	
# Console Class
class Console:
	Mem = Memory()
	
	# Display Messages
	def Display(self, head=None, msg=None, Input=False):
		# Grab Template Core
		temp = self.Mem.MemoryHandler(LOC='setting.temp', ACT='status')
		# Check head Existence 
		Location = 'display.tempalates.'+str(temp)
		Index = self.Mem.MemoryHandler(LOC=Location+':index', ACT='status')
		if head not in Index:
			print ' Failed To Print MSG ...'+str(msg)
			return None
		Message_Head = self.Mem.MemoryHandler(LOC=Location+'.'+str(head), ACT='status')
		MSG = Message_Head+str(msg)
		print MSG
		return None
		
	# Entry Handler
	def EntryHandler(self, CMD, FILTER):
		# Grab Filter Command Entries
		Filters = self.Mem.MemoryHandler(LOC='input.filter:index', ACT='Status')
		# Check Filter Existence 
		if FILTER not in filters:
			self.Display(head='WARN', msg=' Failed To Find Filter ')
			return None
		# Start Parser Based On Filter Index 
		
	# Start Console Object
	def Start(self):
		self.Display(head='BANN')
		Running = True
		while Running == True:
			IO = self.Display(head='INPUT', Input=True)
			FIN = self.EntryHandler(IO, 'CONS')
			if FIN == True:
				Runnning = False
				
		return None 
	
def Main():
	Mem = Memory()
	Cns   = Console()
	Mem.SetUp()
	
	
	
Main()
