import string
from string import *
import random 
from random import *

class nodo:
 def __init__(self,laParola):
  self.par=laParola
  self.link=[]
 def addLink(self,ilNodo2):
  self.link=self.link+[ilNodo2]

learnINP=raw_input('input file to learn: ')
if (learnINP==""):
 learnINP='learningtext.txt'
testo=open(learnINP,'r')
testo_r=lower(testo.read())
testo_r=replace(testo_r,'...',' . ')
testo_r=replace(testo_r,'\n','')
testo_r=replace(testo_r,'.',' . ')
testo_r=replace(testo_r,'','')
testo_r=replace(testo_r,';',' , ')
testo_r=replace(testo_r,',',' , ')
testo_r=replace(testo_r,'.',' END START ')
s=split(testo_r)
s=['START']+s+['END']

START=nodo('START')
END=nodo('END')
dictionary={'START':0,'END':1}
universe=[START,END]

print("learning ")
for k in range(len(s)-1):
 print("learning " + str(100*k/len(s))+"%")
 if (s[k+1] not in dictionary): 
  dictionary[s[k+1]]=len(dictionary) 
  universe=universe+[nodo(s[k+1])]

print "memorizing"
for k in range(len(s)-1): 
  print("memorizing " + str(100*k/len(s))+"%")
  if s[k]=='.' :
   universe[dictionary[s[k]]].addLink(universe[2])
   universe[1].addLink(universe[dictionary[s[k+1]]])
  else:
   universe[dictionary[s[k]]].addLink(universe[dictionary[s[k+1]]])

while True: 
 inp=raw_input('? (use !QUIT! to exit)')
 if (inp=="!QUIT!"):
  break
 else:
     inp=lower(inp) 
 if dictionary.has_key(inp):
  now=universe[dictionary[inp]]
 else:
  inp = 'START'
 
 now = universe[dictionary[inp]]
 speech = ""
 for j in range(100):
  speech = speech + " " + now.par
  
  now=universe[dictionary[now.par]].link[randint( 0, len( universe[dictionary[now.par]].link) - 1)]
  if now == END:
   break
 speech = replace(speech, 'START', '')
 print(speech)
