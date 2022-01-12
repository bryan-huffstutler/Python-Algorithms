import random
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.currentSong = None
        self.currentPlaylist = []
        
    #Complete
    def addSongToList(self, title, artist):
        self.count += 1
        if self.head is None:
            newSong = Song(title, artist)
            self.head = newSong
            self.currentPlaylist.insert(0, newSong)
        else:
            newSong = Song(title, artist)
            self.head.prev = newSong
            newSong.next = self.head
            newSong.prev = None
            self.head = newSong
            self.currentPlaylist.insert(0, newSong)
        self.setTail()
        
    #Complete
    def getSonglist (self):
        for x in self.currentPlaylist:
            print(x)
    
    #Complete        
    def removeSong (self, title, artist):
        self.count -= 1
        temp = self.head
        prev = self.head
        #if current song is being removed
        if self.currentSong.title == title and self.currentSong.artist == artist:
            self.currentSong = None
            
        while temp:
            if temp.title == title and temp.artist == artist:
                if temp == self.head:
                    temp.next.prev = None
                    self.head = temp.next
                else:
                    prev.next = temp.next
                    temp.next = prev
            prev = temp
            temp = temp.next
    
    #Complete         
    def playSong(self):
        self.currentSong = self.head
        return self.currentSong
    
    #Complete
    def skipSong(self):
        temp = self.currentSong
        if temp is None:
            return "No song currently playing...please play a song."
        if temp.next is None:
            self.currentSong = self.head
            return self.head
        else:
            self.currentSong = temp.next
            return self.currentSong
    
    
    def shuffleSongs (self):
        # newList = self.currentPlaylist
        # for x in self.currentPlaylist:
        #     num = random.randint(0, len(self.currentPlaylist)-1)
        #     newList[num].title = x.title
        #     newList[num].artist = x.artist 

        # self.currentPlaylist = newList
        # return self.getSonglist()
        temp=self.head
        while temp:
            if temp is None:
                return
            tempList = self.currentPlaylist
            num = random.randint(0, len(tempList)-1)
            temp.artist = tempList[num].artist
            temp.title = tempList[num].title
            tempList.pop(num)
            temp = temp.next
        return self.getSonglist()
    
    #Complete
    def goBack (self):
        temp = self.currentSong
        if temp is None:
            return "No song currently playing...please play a song."
        if temp.prev is None:
            self.currentSong = self.tail
            return self.currentSong
        else:
            self.currentSong = temp.prev
            return self.currentSong
        
    #Complete
    def setTail(self):
        self.tail = self.currentPlaylist[len(self.currentPlaylist)-1]
    
    #Complete
    def showCurrentSong(self):
        return self.currentSong
    
    
def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

playlist = PlayList()
playlist.addSongToList('Enter Sandman', 'Metallica')
playlist.addSongToList('Everyday', 'Logic')
playlist.addSongToList('Broken', 'Seether')
playlist.addSongToList('Teen Spirit', 'Nirvana')
playlist.addSongToList('Returns', 'NF')
playlist.addSongToList('Lucky You', 'Eminem')
# print(playlist.tail)
while True:
    menu()
    choice = int(input('What would you like to do? '))

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        title = input('What is the name of the song you would like to enter? ')
        artist = input('What is the name of the artist for ' + str(title) + ' : ')
        # Add song to playlist
        playlist.addSongToList(title, artist)
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        title = input('What song would you like to delete? ')
        artist = input('What is the artist name? ')
        # remove song from playlist
        playlist.removeSong(title, artist)
        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")
        print(playlist.playSong())
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")
        print('Now playing...')
        print(playlist.skipSong())                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")
        print(playlist.goBack())  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print(playlist.shuffleSongs())
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")
        print(playlist.showCurrentSong())    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        playlist.getSonglist()
    elif choice == 0:
        print("Goodbye.")
        break