# -*- coding: utf-8 -*-
cars = 100 # hvor mange biler
space_in_a_car = 4.0 # hvor stor plass det er i bilen
drivers = 30 # hvor mange sjaf�rer det er
passengers = 90 # hvor mange pasasjerer det er 
cars_not_driven = cars - drivers # hvor mange biler som ikke kj�rer, biler minus sjaf�rer
cars_driven = drivers # hvor mange biler som kj�rer er det samme som antall sjaf�rer
carpool_capacity = cars_driven * space_in_a_car # hvor mange det er plass til er det samme som biler kj�rt ganger plass i bilen
average_passengers_per_car = passengers / cars_driven # gjennomsnitlig passasjerer per bil er det samme som passasjerer delt p� biler kj�rt


print "There are", cars, "cars available." # viser resultat p� biler
print "There are only", drivers, "drivers available." # viser resultat sjaf�rer
print "There will be", cars_not_driven, "empty cars today." # viser resultat p� biler som ikke kj�rer
print "We can transport", carpool_capacity, "people today." # viser resultat for hvor mange det er plass til
print "We have", passengers, "to carpool today." # viser resultat for passasjerer
print "We need to put about", average_passengers_per_car, "in each car." # viser resultat for gjennomstnitlig passasjerer per bil 