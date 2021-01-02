# My favourite song and artist
#artist = "Don Williams"
#song = "I recall a Gypsy Woman"
#released = 1973
#genre = "Country"
#duration = 3.25
#album = "Volume One"  
#single = "Atta Way to Go"
#chartYear = 73
#chartNum = 13
#chartName = "Hot Country Songs"

# Info above pulled from 1st homework assignment, now refactored into a dictionary format

MyDictionary = {'Artist':'Don Williams', 'Song':'I Recall a Gypsy Woman', 'Release':'1973', 'Genre':'Country', 'Duration':'3.25min', 'Album':'Volume One', 'Single':'Atta Way to Go', 'ChartY':'73', 'ChartNo':'No. 13', 'Chart':'Hot Country Songs'}
for pair in MyDictionary.items():
    print(pair)