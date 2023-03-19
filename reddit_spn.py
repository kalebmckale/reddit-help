from dataclasses import dataclass
import sys


class Octave:
    note_names: str = "CDEFGAB"
    accidentals: dict[str, str] = {"♯": "CF", "♭": "BE"}
    num_semitones: int = 12

"""
WBWBWWBWBWBW

diatonic 
wwh w wwh
whw w whw
hww w hww

chromatic

Mode	Also known as	Starting note relative
to major scale	Interval sequence	Example 1	Example 2
Ionian	Major scale	I	T–T–S–T–T–T–S	C–D–E–F–G–A–B–C	N/A
Dorian		II	T–S–T–T–T–S–T	D–E–F–G–A–B–C–D	C–D–E♭–F–G–A–B♭–C
Phrygian		III	S–T–T–T–S–T–T	E–F–G–A–B–C–D–E	C–D♭–E♭–F–G–A♭–B♭–C
Lydian		IV	T–T–T–S–T–T–S	F–G–A–B–C–D–E–F	C–D–E–F♯–G–A–B–C
Mixolydian		V	T–T–S–T–T–S–T	G–A–B–C–D–E–F–G	C–D–E–F–G–A–B♭–C
Aeolian	Natural minor scale	VI	T–S–T–T–S–T–T	A–B–C–D–E–F–G–A	C–D–E♭–F–G–A♭–B♭–C
Locrian		VII	S–T–T–S–T–T–T	B–C–D–E–F–G–A–B	C–D♭–E♭–F–G♭–A♭–B♭–C
"""

INTERVAL_SEQUENCE = "TTSTTTS"

def get_interval_sequence():
    modes = ("ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian")
    
    for index, mode in enumerate(modes):
        print(
            f"{mode}: {'-'.join(INTERVAL_SEQUENCE[index:])}"
            f"{['', '-'][bool(index)]}{'-'.join(INTERVAL_SEQUENCE[:index])}"
        )

def interval_to_scale(interval, tonic="C"):
    

#f"{name}{accidental}" for name in NAMES


@dataclass(order=True, frozen=True)
class Note:
    frequency: float
    notation: str

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.frequency == other.frequency:
            return True
        return False


class Intervals:

    def __init__(self)

        class Note(NamedTuple):
            name_flat: str
            name_shrp: str
            hz: float

        # init vars
        octave = 0
        count = 0
        self.notes = []
    
        # init note names and interval names
        note = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
        note_en = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

        # 9 octaves of note names in scientific format
        # from C0 to B8
        # ex. A4 is A in the 4th octave, middle A
        A4 = 440     # A440 freq standard 440 Hz
        for number in range(108):

            # note names repeat every 12 notes
            name_index = number % 12

            # creates two equal lists of note names, one with flats, one with sharps
            fname = "%s%d" %(note[name_index], octave)
            sname = "%s%d" %(note_en[name_index], octave)
            # see comments below explaining freqs equation
            freq = A4 * (2**(1/12))**(number-57)
            self.notes.append(Note(fname, sname, freq))

            # each cycle of note names has a unique octave number
            count = count+1
            if count == 12:
                octave = octave+1
                count = 0

            # above freq equation:
            # all notes relative to standard A440 _freqs
            # frequency of a _freqs relative to standard is:
            # ratio = (2^(1/12))^n
            # where n is the # of half-steps from the standard to the _freqs
            # n = k-57 such that n=0 corresponds to A440 with 108 pitches

        # initialize other stuff below
        # .... etc.

    

if __name__ == '__main__':
    sys.exit(0)
    
    # create instance of class
    intervals = Intervals()
    # print note names and frequencies
    for m in range(len(intervals.notes)):
        print(f'{intervals.notes[m][0]}:\t{intervals.notes[m][2]:.2f} Hz')

    # print class name
    print(intervals)
