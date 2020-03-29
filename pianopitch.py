import numpy
from essentia.standard import *
import matplotlib.pyplot as plt
#from music21 import *

# Load audio file; it is recommended to apply equal-loudness filter for PredominantPitchMelodia
loader = EqloudLoader(filename='pianolong.mp3', sampleRate=44100)
audio = loader()
#print("Duration of the audio sample [sec]:")
#print(len(audio)/44100.0)

# Extract the pitch curve
# PitchMelodia takes the entire audio signal as input (no frame-wise processing is required)

pitch_extractor = MultiPitchMelodia(frameSize=4096, hopSize=128)
pitch_values = pitch_extractor(audio) #vector_vector_real

# Pitch is estimated on frames. Compute frame time positions
# pitch_times = numpy.linspace(0.0,len(audio)/44100.0,len(pitch_values) )

# print(len(pitch_values))
timepitcharray = []
valuepitcharray = []
col = 0
for timescale in pitch_values:
    col += 1
    for pitchvalue in timescale:
        print(pitchvalue)
        timepitcharray.append(col)
        valuepitcharray.append(pitchvalue)


plt.plot(timepitcharray, valuepitcharray, 'go')
plt.show()

# pitch_values = [
#                     [1, 2, 3],
#                     [4, 5, 6],
#                     [7, 8, 9],
#                     [10, 11, 12]]
#
# plt.figure()

#tnc = tinyNotation.Converter('6/8 e4. d8 c# d e2.')
#tnc.parse()
#s = tnc.stream
#s.show()

# Plot the estimated pitch contour and confidence over time
#f, axarr = plt.subplots(2, sharex=True)
#axarr[0].plot(pitch_times, pitch_values[0])
#axarr[0].set_title('estimated pitch [Hz]')
#axarr[1].plot(pitch_times, pitch_values[0])
#axarr[1].set_title('pitch confidence')

#plt.figure()
#plt.imshow(pitch_values, interpolation='nearest', cmap=plt.cm.ocean)
#plt.colorbar()

#
print ('end of show')