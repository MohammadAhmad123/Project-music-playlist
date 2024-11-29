
playlist = {}

# Function to add a song to the playlist
def add_song(title, artist, genre):
    try:
        if title in playlist:
            raise ValueError(f"The song '{title}' already exists in the playlist.")
        playlist[title] = {'artist': artist, 'genre': genre}
        print(f"Added '{title}' by {artist} (Genre: {genre}) to the playlist.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Add song operation complete.")


# Function to view the playlist
def view_playlist():
    try:
        if not playlist:
            print("The playlist is empty.")
        else:
            print("\nMusic Playlist:")
            for title, details in playlist.items():
                artist = details['artist']
                genre = details['genre']
                print(f" - {title} by {artist} (Genre: {genre})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("View playlist operation complete.")


# Function to update song information
def update_song(title, new_artist=None, new_genre=None):
    try:
        if title not in playlist:
            raise KeyError(f"The song '{title}' does not exist in the playlist.")
        if new_artist:
            playlist[title]['artist'] = new_artist
        if new_genre:
            playlist[title]['genre'] = new_genre
        print(f"Updated '{title}' in the playlist.")
    except KeyError as e:
        print(f"Error: {e}")
    finally:
        print("Update song operation complete.")




# Function to delete a song from the playlist
def delete_song(title):
    try:
        if title not in playlist:
            raise KeyError(f"The song '{title}' does not exist in the playlist.")
        del playlist[title]
        print(f"Deleted '{title}' from the playlist.")
    except KeyError as e:
        print(f"Error: {e}")
    finally:
        print("Delete song operation complete.")




# Testing the functions
try:
    add_song("Shape of You", "Ed Sheeran", "Pop")
    add_song("Blinding Lights", "The Weeknd", "Synth-pop")
    add_song("Bohemian Rhapsody", "Queen", "Rock")

    view_playlist()

    update_song("Shape of You", new_genre="Dance-pop")
    update_song("Blinding Lights", new_artist="The Weeknd")

    view_playlist()

    delete_song("Bohemian Rhapsody")
    delete_song("Havana")  # Attempt to delete a non-existent song


    view_playlist()
except Exception as e:
    print(f"An unexpected error occurred in the main script: {e}")
finally:
    print("All operations completed.")


print("Adding songs...")
add_song("Shape of You", "Ed Sheeran", "Pop")
add_song("Blinding Lights", "The Weeknd", "Synth-pop")
add_song("Bohemian Rhapsody", "Queen", "Rock")


# Testing the functions
print("Adding songs...")
add_song("Shape of You", "Ed Sheeran", "Pop")
add_song("Blinding Lights", "The Weeknd", "Synth-pop")
add_song("Bohemian Rhapsody", "Queen", "Rock")

print("Viewing playlist...")
view_playlist()

print("Updating songs...")
update_song("Shape of You", new_genre="Dance-pop")
update_song("Blinding Lights", new_artist="The Weeknd")

print("Viewing updated playlist...")
view_playlist()

print("Deleting songs...")
delete_song("Bohemian Rhapsody")
delete_song("Havana")  # Attempt to delete a non-existent song

print("Viewing final playlist...")
view_playlist()







