
from itertools import combinations
from random import choice


class individual:
  
  def __init__(self,genom):
    self.genom = genom


def breeding(p1,p2):
  # make firsts gamets
  g1= [''.join(i)  for i in combinations(p1, (len(p1)// 2
))]

  for c in range(0,len(p1)// 2):
    for i in g1:
      for j in i:
       t = i.lower()
       if (t.count(j.lower())) > 1:
         g1.remove(i)
         break

#make seconds gamets
  g2= [''.join(i)  for i in combinations(p2, (len(p2)// 2
))]

  for c in range(0,len(p2)// 2):
    for i in g2:
      for j in i:
       t = i.lower()
       if (t.count(j.lower())) > 1:
         g2.remove(i)
         break
# make all variations descendants
  f = []
  for i in g1:
    for j in g2:
      f.append(i+j)

  for i in f:
    l = sorted(i, key=str.lower)
    l = ''.join(l)
    f[f.index(i)] = l
  # make ✨beautiful✨ all variations descendants
  f0 = '\n'
  for i in f:
    f0 += i+"\n"
  # make unique descendants
  inPercent = []
  for i in f:
    if i not in inPercent:
      inPercent.append(i)
  # make ✨beautiful✨ unique descendants
  p0 = '\n'
  for i in inPercent:
    p0 += i+"\n"

  
  
  view = "🧬All descendants🧬: {ai}🧫Unique descendants🧫: {ui}🎲Random descendants🎲: {ri}".format(ai=f0,ui=p0,ri=choice(f))
  return view
      
     




