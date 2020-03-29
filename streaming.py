import essentia
from essentia.streaming import *

loader = MonoLoader(filename='piano.mp3')
frameCutter = FrameCutter(frameSize = 1024, hopSize = 512)
w = Windowing(type = 'hann')
spec = Spectrum()
mfcc = MFCC()

pool = essentia.Pool()

mfcc.bands >> None
mfcc.mfcc >> (pool, 'lowlevel.mfcc')

essentia.run(loader)

print ('Pool contains %d', len(pool['lowlevel.mfcc']))