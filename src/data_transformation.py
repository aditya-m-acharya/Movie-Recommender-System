import pandas as pd

class DataTransformation:
    def num_to_cat(users):
        users.replace({'Age':{'1':  "Under 18",
                      '18':  "18-24",
                      '25':  "25-34",
                      '35':  "35-44",
                      '45':  "45-49",
                      '50':  "50-55",
                      '56':  "56 Above"}}, inplace=True)
        users.replace({'Occupation':{'0': "other",
                             '1': "academic/educator",
                             '2': "artist",
                             '3': "clerical/admin",
                             '4': "college/grad student",
                             '5': "customer service",
                             '6': "doctor/health care",
                             '7': "executive/managerial",
                             '8': "farmer",
                             '9': "homemaker",
                             '10': "k-12 student",
                             '11': "lawyer",
                             '12': "programmer",
                             '13': "retired",
                             '14': "sales/marketing",
                             '15': "scientist",
                             '16': "self-employed",
                             '17': "technician/engineer",
                             '18': "tradesman/craftsman",
                             '19': "unemployed",
                             '20': "writer"}}, inplace=True)
        return users
    
    def data_preparation(movies, users, ratings):
        #Using regular expressions to find a year stored between parentheses
        #We specify the parantheses so we don't conflict with movies that have years in their titles
        movies['Year'] = movies.Title.str.extract('(\(\d\d\d\d\))',expand=False)
        #Removing the parentheses
        movies['Year'] = movies.Year.str.extract('(\d\d\d\d)',expand=False)
        #Removing the years from the 'Title' column
        movies['Title'] = movies.Title.str.replace('(\(\d\d\d\d\))', '')
        #Applying the strip function to get rid of any ending whitespace characters that may have appeared
        movies['Title'] = movies['Title'].apply(lambda x: x.strip())
        #dfmov = movies.copy()
        movies.dropna(inplace=True)
        movies.Genres = movies.Genres.str.split('|')
        movies['Genres'] = movies['Genres'].apply(lambda x: [i for i in x if i!='A' and i!='D' and i!= 'F' and i!='C' and i!='M' and i!= 'W' and i!= ' '])
        for i in movies['Genres']:
            for j in range(len(i)):
                if i[j] == 'Ro' or i[j] == 'Rom' or i[j] == 'Roman' or i[j] == 'R' or i[j] == 'Roma':
                    i[j] = 'Romance'
                elif i[j] == 'Chil' or i[j] == 'Childre' or i[j] == 'Childr' or i[j] == "Children'" or i[j] =='Children' or i[j] =='Chi':
                    i[j] = "Children's"
                elif i[j] == 'Fantas' or i[j] == 'Fant':
                    i[j] = 'Fantasy'
                elif i[j] == 'Dr' or i[j] == 'Dram':
                    i[j] = 'Drama'
                elif i[j] == 'Documenta'or i[j] == 'Docu' or i[j] == 'Document' or i[j] == 'Documen':
                    i[j] = 'Documentary'
                elif i[j] == 'Wester'or i[j] == 'We':
                    i[j] = 'Western'
                elif i[j] == 'Animati':
                    i[j] = 'Animation'
                elif i[j] == 'Come'or i[j] == 'Comed' or i[j] == 'Com':
                    i[j] = 'Comedy'
                elif i[j] == 'Sci-F'or i[j] == 'S' or i[j] == 'Sci-' or i[j] == 'Sci':
                    i[j] = 'Sci-Fi'
                elif i[j] == 'Adv'or i[j] == 'Adventu' or i[j] == 'Adventur' or i[j] == 'Advent':
                    i[j] = 'Adventure'
                elif i[j] == 'Horro'or i[j] == 'Horr':
                    i[j] = 'Horror'
                elif i[j] == 'Th'or i[j] == 'Thri' or i[j] == 'Thrille':
                    i[j] = 'Thriller'
                elif i[j] == 'Acti':
                    i[j] = 'Action'
                elif i[j] == 'Wa':
                    i[j] = 'War'
                elif i[j] == 'Music':
                    i[j] = 'Musical'
        df_1 = pd.merge(movies, ratings, how='inner', on='MovieID')
        data = pd.merge(df_1, users, how='inner', on='UserID')
        return data

    def feature_engineering(data):
        data['Datetime'] = pd.to_datetime(data['Timestamp'], unit='s') #Change the datatype from object to date_time
        data['Year']=data['Year'].astype('int32') #Change the datatype from object to Integer
        data['Rating']=data['Rating'].astype('int32') #Change the datatype from object to Integer

        bins = [1919, 1929, 1939, 1949, 1959, 1969, 1979, 1989, 2000]
        labels = ['20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s']
        data['ReleaseDec'] = pd.cut(data['Year'], bins=bins, labels=labels)
        return data

    def data_model_preprocess(data):
        rm = data.pivot(index = 'UserID', columns ='MovieID', values = 'Rating').fillna(0)
        user_itm = data[['UserID', 'MovieID', 'Rating']].copy()
        user_itm.columns = ['UserId', 'ItemId', 'Rating']
        return user_itm, rm