from Clock import timer
from Parse import *
import datetime
from Reservatiesysteem import Reservatiesysteem

functions = {'zaal': 'addZaal','film': 'addFilm','vertoning': 'addVertoning','gebruiker': 'addGebruiker','reserveer': 'addReservatie','ticket': 'updateTickets'}

class Perform:
    def __init__(self, filename: str):
        pars = Parse(filename)
        # INFORMATIE LEZEN EN IN EEN DICTIONARY
        self.parsed = pars.parse()
        # RUNT ALLES
        self.run()
    def run(self):
        for line in self.parsed:
            # WACHT ALS ER OP EEN TIJDSTIP GEWACHT MOET WORDEN
            if 'time' in line:
                self.await_(line['time'])
                if line['cmd'] == 'reserveer':
                    line['args'].insert(0, line['time'])
            timer.toggle()  # SCHAKELT KLOK UIT

            # FUNCTIE ZONDER PARAMETERS UITVOEREN
            if len(line['args']) == 0:
                eval('self.' + line['cmd'] + '()')
                continue

            # FUNCTIE UITPRINTEN (+ DATUM EN TIJD UITPRINTEN ALS DE KLOK GESTART IS !)
            if timer.isInitialized():
                print(f"{timer} Kinepolis", functions[line['cmd']] + str(tuple(line['args'])))
            else:
                print(functions[line['cmd']] + str(tuple(line['args'])))

            # VOER DE MAIN FUNCTIE UIT MET eval(function)!
            eval('self.r.' + functions[line['cmd']] + str(tuple(line['args'])))
            timer.toggle() # SCHAKELT KLOK AAN
    def init(self):
        print("------------------------------------------------------------------------")
        print("\033[1;34m            Kinepolis Reservatie systeem geïnitialiseert\033[0m")
        print("------------------------------------------------------------------------")
        self.r = Reservatiesysteem()
    def await_(self, time: datetime.datetime):
        timer.setTime(time)
    def start(self):
        print("------------------------------------------------------------")
        print("\033[1;34m           Kinepolis Reservatie systeem gestart\033[0m")
        print("------------------------------------------------------------")
        dt = datetime.datetime(2023, 10, 5)
        dt = dt.replace(hour=8, minute=0, second=0, microsecond=0)
        timer.setTime(dt)
        timer.start()

    def log(self):
        print("----------------------------------------------------------")
        print(f"\033[1;32m          {timer} Kinepolis LOG\033[0m")
        print("----------------------------------------------------------")
        self.r.log(str(timer))

system = Perform('new_system.txt')