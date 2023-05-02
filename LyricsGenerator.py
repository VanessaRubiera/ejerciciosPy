# Programa para ver lyrics de canciones 

# Define la lista de canciones y sus letras
song_lyrics = {
    'Baby by Bieber': "You know you love me, I know you care...",
    'Hotline Bling by Drake': "You used to call me on my cellphone...",
    'Flawless by Beyonce': "I'm out that H, town coming coming down...",
    'Fall by Eminem': "How come you can be a Christian, a veterinarian, a homosexual, a racist...",
    'Bohemian Rhapsody by Queen': "Is this the real life? Is this just fantasy?...",
    'Thriller by Michael Jackson': "It's close to midnight, and something evil's lurking...",
    'Smells Like Teen Spirit by Nirvana': "Load up on guns, bring your friends...",
    'Stairway to Heaven by Led Zeppelin': "There's a lady who's sure all that glitters is gold...",
    'Imagine by John Lennon': "Imagine there's no heaven, it's easy if you try...",
    'Like a Rolling Stone by Bob Dylan': "Once upon a time you dressed so fine, you threw the bums a dime..."
}

# Pide al usuario que elija una canción
print("Bienvenido, por favor selecciona una canción de las siguientes 10 canciones:\n")
while True:
    for i, song in enumerate(song_lyrics.keys()):
        print(f"{i+1}. {song}")
    print()
    choice = input("Ingresa el número de la canción que te gustaría ver la letra: ")
    if choice == "*":
        continue
    elif choice.isdigit() and 1 <= int(choice) <= len(song_lyrics):
        break
    else:
        print("Opción inválida. Por favor ingresa un número entre 1 y 10 o * para volver a elegir.\n")

# Imprime la letra de la canción seleccionada
song = list(song_lyrics.keys())[int(choice)-1]
print(f"\n------- {song} ------------")
print(song_lyrics[song])

# Pregunta si el usuario quiere ver más canciones del mismo artista
artist = song.split(' by ')[1]
while True:
    choice = input(f"\n¿Te gustaría ver más canciones de {artist}? (s/n) ")
    if choice.lower() == "s":
        # Imprime todas las canciones del mismo artista
        print(f"\nAquí están todas las canciones de {artist}:")
        for s in song_lyrics.keys():
            if s.endswith(f"by {artist}"):
                print(f"- {s}")
        # Pide al usuario que elija otra canción del mismo artista
        while True:
            choice = input("\nIngresa el número de la canción que te gustaría ver la letra: ")
            if choice == "*":
                break
            elif choice.isdigit():
                choices = [i+1 for i, s in enumerate(song_lyrics.keys()) if s.endswith(f"by {artist}")]
                if int(choice) in choices:
                    song = list(song_lyrics.keys())[choices.index(int(choice))]
                    print(f"\n------- {song} ------------")
                    print(song_lyrics[song])
                    break
            print("Opción inválida. Por favor ingresa un número entre 1 y el número de canciones del artista o * para volver a elegir.")
        # Si el usuario elige ver más canciones, continúa el ciclo
        continue
    elif choice.lower() == "n":
        break
    else:
        print("Opción inválida, por favor ingresa \"y\" or \"n\".\n")

print("\nGracias por usar el programa generador de lyrics!")