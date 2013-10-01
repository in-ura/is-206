# -*- coding: utf-8 -*-
cars = 100 # hvor mange biler
space_in_a_car = 4.0 # hvor stor plass det er i bilen
drivers = 30 # hvor mange sjafører det er
passengers = 90 # hvor mange pasasjerer det er 
cars_not_driven = cars - drivers # hvor mange biler som ikke kjører, biler minus sjafører
cars_driven = drivers # hvor mange biler som kjører er det samme som antall sjafører
carpool_capacity = cars_driven * space_in_a_car # hvor mange det er plass til er det samme som biler kjørt ganger plass i bilen
average_passengers_per_car = passengers / cars_driven # gjennomsnitlig passasjerer per bil er det samme som passasjerer delt på biler kjørt


print "There are", cars, "cars available." # viser resultat på biler
print "There are only", drivers, "drivers available." # viser resultat sjafører
print "There will be", cars_not_driven, "empty cars today." # viser resultat på biler som ikke kjører
print "We can transport", carpool_capacity, "people today." # viser resultat for hvor mange det er plass til
print "We have", passengers, "to carpool today." # viser resultat for passasjerer
print "We need to put about", average_passengers_per_car, "in each car." # viser resultat for gjennomstnitlig passasjerer per bil 