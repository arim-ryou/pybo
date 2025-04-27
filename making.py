
import pandas as pd
from app.models import Book

filename = 'Book_list.xlsx'

for i in range(1,24):
    data_sheet = pd.read_excel(filename, engine='openpyxl',  sheet_name = '책장 %d' %i  )
    
    for j in data_sheet.index:
        if data_sheet['Completed'][j]  == '완결':
            complite = True
        else:
            complite = False

        if str(data_sheet['Author'][j]) == 'nan':
            Author = ' '
        else:
            Author = data_sheet['Author'][j]

        book = Book(title =  data_sheet['Title'][j], author = Author, is_complete = complite, shelf_number = int(data_sheet['Shelf'][j].replace('-', '')))
        book.save()




