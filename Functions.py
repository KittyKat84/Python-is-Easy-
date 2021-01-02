# artist = "Don Williams"
# song = "I recall a Gypsy Woman"
# album = "Volume One" 

def artist(Name):
    output = print("The artists name is " + Name)
    return output

Name = "Don Williams"
artistName = artist(Name)
print (artistName)

def song(Title):
    output = print("The song title is " + Title)
    return output

Title = "I recall a Gypsy Woman"
songTitle = song(Title)
print(songTitle)

def album (Cover):
    output = print("His first album was called " + Cover)
    return output

Cover = "Volume One"
albumCover = album(Cover)
print(albumCover)