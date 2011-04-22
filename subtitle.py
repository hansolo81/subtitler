import os
import glob

fp = 'F:\\Series\\Breaking Bad'

mkvs = []
sub = []

for m in glob.glob(os.path.join(fp, '*.avi')):
    mkvs.append(m.replace('.avi', ''))

mkvs = sorted(mkvs)
print mkvs
for f in sorted(glob.glob(os.path.join(fp, '*.srt'))):
    print f
    os.rename(f, '%s.srt' % mkvs.pop(0))

    
