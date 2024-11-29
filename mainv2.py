# Initialize an empty dictionary to store the playlist data.
playlist = {} 

# Function to create and add songs to the playlist.
def create_a_songlist():
    print("Add a song to the dictionary\n")
   
    while True:  # Infinite loop to keep adding songs until the user decides to stop.
        # Create a template for each song with default empty values.
        songlist = {
            "songID": "",
            "Artist": "",
            "song name": "",
            "genre": ""
        }
       
        try:
            # Iterate through each key in the song dictionary (songID, Artist, etc.).
            for aKey in songlist:
                while True:  # Loop to ensure valid input for each field.
                    try:
                        # Prompt user for input based on the current key.
                        aValue = input(f"Enter the value for {aKey}: ")
                        
                        # Check if the songID already exists in the playlist.
                        if aKey == "songID" and aValue in playlist:
                            raise ValueError(f"The song with ID '{aValue}' already exists.")
                        
                        # Commented-out validation code for genre (example for future validation logic).
                        # if aKey == "genre":   
                        #     if not aValue.isdigit() or int(aValue) <= 0:
                        #         raise ValueError("Genre must be a positive integer value.")  
                        
                        # Add the user input to the current song's key.
                        songlist[aKey] = aValue
                        break  # Exit the input loop for this key if successful.
                    except ValueError as ve:
                        print(f"Error because of: {ve}")
                  
            # Add the completed song dictionary to the playlist using songID as the key.
            playlist[songlist["songID"]] = songlist
            print(f"Added: {songlist}")
 
            # Ask the user if they want to add another song.
            another_song = input("\nAdd another song? (yes/no): ").lower()
            if another_song != "yes":
                break  # Exit the main loop if the user doesn't want to add more songs.
         
        except ValueError as ve:
            print(f"Error because of: {ve}")
        except Exception as e:
            print(f"Error because of: {e}")
        finally:
            print("Operation completed...\n")  # Executed at the end of each loop iteration.

# Function to retrieve and display song details by songID.
def useID(songID):
    # Try to get the song details from the playlist.
    songlist = playlist.get(songID)
    if songlist:  # If the song is found, print the details.
        print(f"Found: {songlist}")
    else:  # If not found, display an appropriate message.
        print(f"Not Found")

# Function to delete a song from the playlist by songID.
def delete_song(songID):
    try:
        # Check if the songID exists in the playlist.
        if songID in playlist:
            deleted_song = playlist.pop(songID)  # Remove the song from the playlist.
            print(f"Deleted: {deleted_song}")
        else:
            raise KeyError(f"No song found with ID '{songID}'.")  # Raise an error if songID is not found.
    except KeyError as e:
        print(f"Error: {e}")
    finally:
        print("Delete operation completed.\n")  # Executed at the end of the delete operation.

# Call the function to start creating the songlist.
create_a_songlist()

# Print the current playlist.
print("\nCurrent Playlist:")
print(playlist)

# Prompt the user to search for a song by its ID.
songID = input("\nEnter the song ID to find its details: ")
useID(songID)

# Prompt the user to delete a song by its ID.
delete_id = input("\nEnter the song ID to delete: ")
delete_song(delete_id)

# Print the final playlist after deletion.
print("\nFinal Playlist:")
print(playlist)



