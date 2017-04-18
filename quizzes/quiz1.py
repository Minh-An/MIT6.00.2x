#Quiz Problem 3


def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = [songs[0][0]]
    if songs[0][2] > max_size:
        return []
    songsLeft = songs[1:]
    sizeLeft = max_size - songs[0][2]
    while True:
        smallest = ('', 0, False)
        for song in songsLeft: 
            if song[2] <= sizeLeft:
                if song[1] < smallest[2] or smallest[2] == False:
                    smallest = song
        if smallest[2] == False:
            break
        playlist.append(smallest[0])
        sizeLeft -= smallest[2]
        songsLeft.remove(smallest)
    return playlist

#songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
#print(song_playlist(songs, 12.2))
#print(song_playlist(songs, 11))

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    remainingSum = s
    multipliers = []
    for n in L:
        m = remainingSum//n
        multipliers.append(m)
        remainingSum -= n * m
    if sum([L[i] * multipliers[i] for i in range(len(L))]) == s:
        return sum(multipliers)
    else:
        return "no solution"
    
#print(greedySum([5,3,2], 16))
#print(greedySum([5,3,2], 13))
#print(greedySum([5,3,1], 14))
#print(greedySum([5,2,1], 11))
#print(greedySum([5,2,1], 13))

def all_contiguous_subsequences(L):
    subsequences = []
    for i in range(len(L)):
        for j in range(i, len(L)+1):
            if L[i:j] != []:
                subsequences.append(L[i:j])
    return subsequences

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    subsequences = all_contiguous_subsequences(L)
    maximum = 0
    for subsequence in subsequences:
        if sum(subsequence) > maximum:
            maximum = sum(subsequence)
    return maximum
    
print(max_contig_sum([3,-3,-3,-3]))
    
    
    
    
    
    
    