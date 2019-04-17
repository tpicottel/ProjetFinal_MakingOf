# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier = "markscheiffele.csv"

entetes = {
	"User-Agent":"Julien Latraverse - request for a journalism project",
		"From":"j.lat@hotmail.ca"
}


p = ["Annee","Choix_au_repechage","Equipe_de_repechage", "Nom_du_joueur", "Position", "Parties_jouees", "Points", "Pays", "Equipe", "Ligue"]

saku = open(fichier,"a")
koivu = csv.writer(saku)
koivu.writerow(p)

for annee in range (2004,2019):
	url = "https://www.hockey-reference.com/draft/NHL_{}_entry.html".format(annee)
	print(url)

	contenu = requests.get(url, headers=entetes)

	page = BeautifulSoup(contenu.text,"html.parser")

	s = []

	print()
	joueurs = page.find_all("tr")
	for joueur in joueurs :
		s =[]
		try:
			gamesplayed = joueur.find('td',attrs={"data-stat":"games_played"}).text
			nomjoueur = joueur.find('td',attrs={"data-stat":"player"}).text
			drafteam = joueur.find('td', attrs={"data-stat":"team_name"}).text
			pays = joueur.find('td',attrs={"data-stat":"birth_country"}).text
			pick = joueur.find('th',attrs={"data-stat":"pick_overall"}).text
			team = joueur.find('td',attrs={"data-stat":"amateur_team"}).text
			team = team.split("(")
			equipe = team[0].strip()
			ligue = team[1].replace(")", "").strip()
			points = joueur.find('td',attrs={"data-stat":"points"}).text
			pos = joueur.find('td',attrs={"data-stat":"pos"}).text
			if gamesplayed == "" : 
				gamesplayed = 0
			else:
				gamesplayed = int(gamesplayed)
			if points == "":
				points = 0
			else:
				points = int(points)
		except:
			gamesplayed = ""
			nomjoueur = "ROUND"
			pays = equipe = ligue = points = pos = drafteam = pick = ""

		s.append(annee)
		s.append(pick)
		s.append(drafteam)
		s.append(nomjoueur)
		s.append(pos)
		s.append(gamesplayed)
		s.append(points)
		s.append(pays)
		s.append(equipe)
		s.append(ligue)

		saku = open(fichier,"a")
		koivu = csv.writer(saku)
		koivu.writerow(s)

		print(annee,pick,drafteam,nomjoueur,pos,gamesplayed,points,pays,equipe,ligue)
	
	# print(page.find_all('td',attrs={"data-stat":"games_played"}))



