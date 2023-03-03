#testcodes
import Reservatiesysteem
from Film import *
from Gebruiker import *
from Vertoning import *
from Zaal import *
from Reservatie import *

from Reservatiesysteem import *

r = Reservatiesysteem()
print()
r.addGebruiker(1,"sejar","dindar","sejar@10")
print()
r.addFilm(1,"thematrix",6.1)
print()
r.addReservatie(1,"TG","12","1","4")
print()
r.addVertoning(1,20,4,"2 oktober", 1)
print()
r.addZaal(10,200)