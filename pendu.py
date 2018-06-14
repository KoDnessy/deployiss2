#!/usr/bin/python2.7
# -*-coding:utf-8 -*


import random

class joueur ():

	def __init__(self):

		self.nomdujoueur= "Bobby"
		self.nombredepartie= 0
		self.nombredevictoire = 0
		self.nombrededefaite = 0

	def victoire(self):
		self.nombredevictoire += 1
		print (self.nombredevictoire)

	def defaite(self):
		self.nombrededefaite += 1
		print (self.nombrededefaite)

	def partie(self):
		self.nombredepartie +=1
		print (self.nombredepartie)




####-------------------Generation de la liste de mot test du pendu-------------------------
basededonnemots = ["arbre", "cacao", "poils", "choux", "salut", "chien", "loups", "maman"]
print (basededonnemots)
####-------------------On genere un nombre aleatoire pour choisir un mot dans la liste
hasard = random.randrange(0,7)
motadecouvrir = basededonnemots [hasard]
print (motadecouvrir)
####-------------------On a diviser le mot en chaine de caractere
motadecouvrirlist = list(motadecouvrir)
print (motadecouvrirlist)


lettre = "a"
# print (place)

lettredejadite= []
flagdemottrouve = 0
print ("Le mot au hasard est genere")
flagdejadit = False
motcacher = ["*"]
i = 0
gagner = 0
perdu = 0
nbechec = 0
difficulte = 5
lettretrouver = 0
nbechec = difficulte

while i < (len(motadecouvrirlist)-1):
	motcacher.append ("*")
	i += 1


while flagdemottrouve == 0 :
	print (motcacher)	
	print ("Il vous reste {} essai".format(nbechec))
	print ("Voila les lettre que vous avez deja dit ")
	print (lettredejadite)
	print ("quel est la lettre que vous tester ?")
	lettre = input("la lettre :")
	#print (lettre)
	place = (motadecouvrir.find(lettre))
	#print ("Voila la place de la lettre dans le mot : {}".format(place+1))
	count = (motadecouvrir.count(lettre))
	#print (count)
	print ("Voila le nombre de fois qu il y a {} dans le mot {} : {}".format(lettre, motadecouvrir, count ))

	flagdejadit = lettre in lettredejadite
	if flagdejadit == False :
		if place != -1:
			lettredejadite.append(lettre)
			while count != 0 :
				print ("La lettre existe elle est en {} place ".format(place+1))
				motcacher[place]=lettre
				count -= 1
				place = (motadecouvrir.find(lettre, place+1))
				lettretrouver += 1
		 
		else :
			print ("La lettre n existe pas dans le mot vous avez perdu un essai")
			lettredejadite.append(lettre)
			nbechec -= 1
	else :
		print ("Vous avez deja dit cette lettre")

	if lettretrouver == (len(motadecouvrirlist)):
		print ("Vous avez trouver toutes les lettres du mot")
		gagner = 1
		flagdemottrouve = 1
	else :
		print ("Vous n avez pas encore trouve le mot")

	if nbechec == 0:
		print ("Vous n' avez plus assez d essai ")
		perdu = 1
		flagdemottrouve = 1
	else :
		print ("")


if gagner == 1 :
	print ("Vous avez gagne")
else :
	print ("")

if perdu == 1 :
	print ("Vous avez perdu")
else :
	print ("")


a = input()





