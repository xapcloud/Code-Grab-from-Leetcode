

f = open('leetcode','wb')
f.write('---\n')
f.write('title:『Leetcode』All AC Leetcode Subjects and Solutions')
f.write('---\n')

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
		f.write('['+allDir+']')        



eachFile('/Users/xyma/Documents/Blog/source/leetcode_with_solution/')
