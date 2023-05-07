import pandas as pd

from Reservatiesysteem import *

filmlist = ["hello","hello","hello"]
idlist = [1,2,3]
zaallist = [4,5,6]

my_dict = {
    'MOVIE': filmlist,
    'ID': idlist,
    'ZAAL':zaallist
#    'TIJD': [30, 40, 50],
#   'ZAAL': [1, 2, 3]
}
my_data = pd.DataFrame(data=my_dict)
my_data.to_html('C:/Users/aboba/PycharmProjects/MainTOg/abu.html',index = False)
