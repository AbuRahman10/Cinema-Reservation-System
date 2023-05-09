from Clock import timer
from Parse import *
import datetime
from Reservatiesysteem import Reservatiesysteem

functions = {
    'zaal': 'addZaal',
    'film': 'addFilm',
    'vertoning': 'addVertoning',
    'gebruiker': 'addGebruiker',
    'reserveer': 'addReservatie',
    'ticket': 'updateTickets'}

class Perform:
    def __init__(self, filename: str):
        pars = Parse(filename)
        self.parsed = pars.parse()  # parsed de filename
        self.run()  # runt de parsed file

    def run(self):
        for line in self.parsed:
            if 'time' in line:  # wacht als er op een tijdstip gewacht moet worden
                time1 = line['time']
                self.await_(line['time'])
                if line['cmd'] == 'reserveer':
                    line['args'].insert(0, line['time'])

            timer.toggle()  # schakelt de klok uit

            if len(line['args']) == 0:
                function = 'self.' + line['cmd'] + '()'
                eval('self.' + line['cmd'] + '()')
                continue  # for loop gaat door naar de volgende 'line'

            # FUNCTIE UITPRINTEN (+ DATUM EN TIJD UITPRINTEN ALS DE KLOK GESTART IS !)
            if timer.isInitialized():
                function1 = f"{timer} Cinema$", functions[line['cmd']] + str(tuple(line['args']))
                print(f"{timer} Kinepolis", functions[line['cmd']] + str(tuple(line['args'])))
            else:
                function2 = functions[line['cmd']] + str(tuple(line['args']))
                print(functions[line['cmd']] + str(tuple(line['args'])))

            function3 = 'self.r.' + functions[line['cmd']] + str(tuple(line['args']))
            eval('self.r.' + functions[line['cmd']] + str(tuple(line['args'])))  # self.r.func(args)

            timer.toggle()  # zet de klok terug aan

    def init(self):
        print(f"Initializing Reservatie systeem")
        self.r = Reservatiesysteem()

    def start(self):
        # setup the clock
        print("Starting Reservatie systeem")
        dt = datetime.datetime(2023, 10, 5)
        dt = dt.replace(hour=8, minute=0, second=0, microsecond=0)
        timer.setTime(dt)
        timer.start()

    def log(self):
        print(f"{timer} Kinepolis", "log")
        self.r.log(str(timer))

    def await_(self, time: datetime.datetime):
        timer.setTime(time)  # sets clock time to desired time


e = Perform('new_system.txt')