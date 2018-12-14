import numpy as np
import midi_manipulation
import glob
from tqdm import tqdm

def get_songs(directory_path):
    files = glob.glob('{}/*.mid'.format(directory_path))
    songs = []
    for f in tqdm(files):
        try:
            song = np.array(midi_manipulation.midiToNoteStateMatrix(f))
            if np.array(song).shape[0] > 50:
                songs.append(song)
        except Exception as e:
            raise e
    return songs

songs = get_songs('resources') #These songs have already been converted from midi to msgpack
print("{} songs processed".format(len(songs)))
###################################################

def main():
    print(songs)











if __name__ == '__main__':
    main()