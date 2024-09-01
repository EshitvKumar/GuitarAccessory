MIDDLE_C = 440 * (2 **(-9 / 12))
ALL_NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

GUITAR_NOTES = ["E2", "A2", "D3", "G3", "B3", "E4"]

def noteToPitch(a: str) -> float:
  noteLetter = a[: -1]
  noteNum = int(a[-1])

  octaveExp = (noteNum - 4) * 12
  noteShift = ALL_NOTES.index(noteLetter) # i for 2**i/12

  retPitch = MIDDLE_C * (2 ** ((octaveExp + noteShift) / 12))

  return retPitch

#this is anyway sorted from lowest pitch to highest
GUITAR_PITCHES = [noteToPitch(i) for i in GUITAR_NOTES]

def compareTwoInd(a, b, target):
    if (target - a) > (b - target):
        return b, 1
    else:
        return a, 0

def getClosestGuitarNote(pitch):
    if pitch < GUITAR_PITCHES[0]:
       return GUITAR_PITCHES[0], GUITAR_NOTES[0]
    
    if pitch > GUITAR_PITCHES[-1]:
       return GUITAR_PITCHES[-1], GUITAR_NOTES[-1]
    
    l, r = 0, 6

    while l < r:
        m = (l + r) // 2
        if GUITAR_PITCHES[m] == pitch:
            return GUITAR_PITCHES[m], GUITAR_NOTES[m]
        
        if (pitch < GUITAR_PITCHES[m]):

            if (m > 0 and pitch > GUITAR_PITCHES[m - 1]):
                retPitch, shift = compareTwoInd(GUITAR_PITCHES[m - 1], GUITAR_PITCHES[m], pitch)
                return retPitch, GUITAR_NOTES[m - shift]

            r = m

        else:
            if (m < 6 - 1 and pitch < GUITAR_PITCHES[m + 1]):
                retPitch, shift = compareTwoInd(GUITAR_PITCHES[m - 1], GUITAR_PITCHES[m], pitch)
                return retPitch, GUITAR_NOTES[m - shift]

            l = m + 1

    return GUITAR_PITCHES[m], GUITAR_NOTES[m]