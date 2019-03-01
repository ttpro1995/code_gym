from collections import Counter

__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"
__link__ = "https://www.codewars.com/kata/which-filetypes-are-you-using-the-most"

def solve(files):
    if len(files) == 0:
        return []
    cnt = Counter()
    for file in files:
        cnt[get_extension(file)]+= 1
    most_common = cnt.most_common()
    top = most_common[0][1]
    common_ext = []
    for e in most_common:
        if (e[1]==top):
            common_ext.append(e[0])
    return sorted(common_ext, reverse=False)


def get_extension(filename):
    names = filename.split(".")
    extension = names[-1]
    return "."+extension


r = solve(['direful.pr', 'festive.html', 'historical.wav', 'holistic.mp3', 'impossible.jar', 'gentle.cpp', 'gleaming.xml', 'inconclusive.js', 'erect.jar', 'befitting.mp3', 'brief.wp', 'beautiful.jar', 'energetic.pt', 'careful.wp', 'defective.cpp', 'icky.wav', 'gorgeous.txt', 'good.pt', 'fat.pt', 'bored.als', 'adaptable.cpp', 'fumbling.exe', 'grieving.wp', 'efficient.wav', 'fearful.xml', 'damp.html', 'erect.exe', 'annoyed.xml', 'elderly.ala', 'far-flung.txt', 'careful.mp3', 'actually.pt', 'cynical.ala', 'complex.exe', 'extra-small.pt', 'enchanted.ala', 'amazing.html', 'bashful.h', 'hallowed.html', 'entertaining.html', 'bad.js', 'illegal.maya', 'deadpan.html', 'furtive.wp', 'hanging.css', 'drunk.py', 'capricious.wav', 'damaging.Ue4', 'cool.Ue4', 'ambitious.css', 'fortunate.wp', 'electric.mp3', 'crowded.txt', 'cooperative.html', 'graceful.pt', 'aboard.pt', 'exclusive.als', 'glossy.css', 'fluffy.pt', 'cluttered.txt', 'halting.cpp', 'glib.cpp', 'aback.pr', 'cynical.Ue4', 'chilly.xml', 'hideous.ala', 'finicky.txt', 'feigned.ala', 'better.Ue4', 'dear.py', 'available.xml', 'easy.pr', 'fine.mp3', 'cowardly.jar', 'incredible.css', 'adhesive.exe', 'energetic.mp3', 'harmonious.exe', 'general.als', 'condemned.als', 'flawless.als', 'curvy.h', 'ambitious.mp3', 'disillusioned.xml', 'bitter.h', 'hanging.wp', 'certain.cpp', 'flashy.html', 'cuddly.pr', 'cagey.Ue4', 'extra-small.pr', 'amuck.cpp', 'direful.html', 'delightful.als', 'helpless.h', 'foamy.mp3', 'enthusiastic.maya', 'good.maya', 'adhesive.css', 'imperfect.pr', 'bent.cpp', 'exultant.zbrush', 'adorable.mp3', 'clammy.maya', 'gaudy.pt', 'blushing.css', 'cuddly.Ue4', 'curved.py', 'boring.html', 'broken.txt', 'daily.jar', 'giddy.xml', 'curved.css', 'future.maya', 'graceful.css', 'guiltless.maya', 'gentle.cpp', 'few.css', 'calculating.txt', 'clear.pr', 'grey.py', 'entertaining.ala', 'elfin.txt', 'excited.js', 'abject.zbrush', 'best.js', 'boundless.wav', 'hurried.ala', 'delirious.cpp']
)

print(r)