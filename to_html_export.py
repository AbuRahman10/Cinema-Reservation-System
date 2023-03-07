import pandas as pd

my_dict = {
    'MOVIE': ['THE Matrix', 'Up', 'Maze Runner'],
    'ID': [1, 2, 3],
    'TIJD': [30, 40, 50],
    'ZAAL': [1, 2, 3]
}
my_data = pd.DataFrame(data=my_dict)
my_data.to_html('C:/Users/thomg/PycharmProjects/SCHOOL/MainTOg/test.html',index = False)
