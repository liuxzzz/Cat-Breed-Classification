#  data set https://www.kaggle.com/datasets/zippyz/cats-and-dogs-breeds-classification-oxford-dataset/code?datasetId=137362&sortBy=dateRun&tab=profile

import os 
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGS_PATH = 'images/images'
print(ROOT)



all_imgs = [i for i in os.listdir(IMGS_PATH) if i.rsplit('.',1)[1] == 'jpg' ]



l = open(ROOT + '/annotations/annotations/list.txt', 'r')

get_breed = lambda pic : pic.rsplit('_',1)[0].lower()
get_species = lambda num : 'cat' if num==1 else 'dog'


info_by_id = {}
info_by_breed = {}


for line in l:
  
  if line[0] == '#':
    continue
  
  line = line.strip().split(' ')
  
  species = get_species(int(line[2]))
  id = int(line[1])
  breedid = int(line[3])
  name = get_breed(line[0]).lower()
  
  if name not in info_by_breed:
    info_by_breed[name] = {'breed' : name, 'species' : species, 'globalid': id, 'breedid':breedid, 'count':0}
    info_by_id[id] = info_by_breed[name]

for p in [get_breed(n) for n in   all_imgs ]:
  info_by_breed[p]['count']+=1



with open(ROOT + '/annotations.json', 'w') as f:
  json.dump(info_by_id, f, indent=2)   