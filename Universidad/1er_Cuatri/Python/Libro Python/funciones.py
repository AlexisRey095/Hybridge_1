
#? Ejercicio1_Album

def make_album(artist_name, album_name, qtt_songs=None):
    artist = {'namer':artist_name, 'album':album_name}
    if qtt_songs:
        artist['Songs']=qtt_songs
    return artist

all_albums = []

while True:
    
    qtt_songs = None #! >> Si no se define la variable con None da error
    artist = input('\nInsert the Artist Name: ')
    album = input('Inser album name: ')
    question_songs = input('Do you know how many song are on the album?(y/n): ')
    if question_songs.lower() == 'y':
        qtt_songs = input('How many song?: ')
    else:
        pass

    if qtt_songs:
        musician = make_album(artist, album, qtt_songs)
        all_albums.append(musician)
    else:
        musician = make_album(artist, album)
        all_albums.append(musician)

    exit_program = input('Do you wanna leave? (y/n)')
    
    if exit_program == 'y':
        break

for a in all_albums:
    print(a)
