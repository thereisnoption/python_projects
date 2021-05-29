def make_album(artist, title, number_of_songs=None):
	if number_of_songs:
		albums = {'artist': artist, 'album_title': title, 'number_of_songs': number_of_songs}
	else:
		albums = {'artist': artist, 'album_title': title}

	return albums

while True:
	print("\nPlease tell me your album: ")
	print("(press 'q' at any time to quit)")

	artist = input("Artist: ")
	if artist.lower() == "q":
		break

	album = input("Album: ")
	if album.title() == "q":
		break

	songs = input("The number of songs: ")
	if songs.lower() == "q":
		break

	formatted_album = make_album(artist, album, number_of_songs=songs)
	print(formatted_album)