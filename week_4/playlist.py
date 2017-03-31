# Class Playlist is a type that we are creating to interact with class Song.
# Initially, the Playlist objet will have a title, but will not contain any songs.
# The constructor will only take as input the name of the Playlist and create an empty list for the songs.

import song

class Playlist:

    def __init__(self, title):
        """ (Playlist, str) -> NoneType

        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.title
        'Canadian Artists'
        >>> playlist.songs
        []
        """

        self.title = title
        self.songs = []

    def add(self, song):
        """ (Playlist, Song) -> NoneType

        Add song to this playlist.

        >>> stompa = song.Song("Serena Ryder", "Stompa", 3, 15)
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(stompa)
        >>> playlist.songs[0] == stompa
        True
        """

        self.songs.append(song)

    def get_duration(self):
        """ (Playlist) -> (int, int)

        Return the duration of this playlist as tuple of minutes and
        seconds.

        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15))
        >>> playlist.get_duration()
        (8, 18)
        """

        total_minutes = 0
        total_seconds = 0

        for song in self.songs:
            total_minutes += song.minutes
            total_seconds += song.seconds

        return (total_minutes + total_seconds // 60,  total_seconds % 60)

    def __str__(self):
        """ (Song) -> str

        Return a string representation of this playlist.

        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 15))
        >>> print(playlist)
        Canadian Artists (8:18)
        1. Neil Young, Harvest Moon (5:03)
        2. Serena Ryder, Stompa (3:15)
        """

        duration = self.get_duration()
        minutes = str(duration[0])
        seconds = str(duration[1]).rjust(2, '0')

        result = self.title + ' (' + minutes + ':' + seconds + ')'

        # Append the songs in the playlist.
        song_num = 1
        for song in self.songs:
            result += '\n' + str(song_num) + '. ' + str(song)
            song_num += 1

        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    playlist = Playlist('Canadian Artists')
    playlist.add(song.Song("Neil Young", "Harvest Moon", 5, 3))
    playlist.add(song.Song("Serena Ryder", "Stompa", 3, 15))
    playlist.add(song.Song("Stompin' Tom Connors", "The Hockey Song", 2, 17))
    print()
    print(playlist)
    print()
