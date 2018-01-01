import json
import requests

class OWInfo:

    def populate(self):
        data = dict()
        hero_r = requests.get(self.api_index['api.hero.index']).json()
        hero_r_data = hero_r['data'] 
        for x in range(0,hero_r['total'] - 1):
            data[hero_r_data[x]["name"]] = hero_r_data[x]['url']
        return data

        #map_r = requests.get(self.api_index['api.map.index']).json()
        #map_r_data = map_r['data'] 
        #for x in range(0,map_r['total']-1):
        #    data[map_r_data[x]["name"]] = map_r_data[x]['url']
        
        #self.api_map_index = data

    

    def create(self):
        print('Ow created')
        self.headers = {'Accept': 'application/json'}
        self.api_index = requests.get('http://overwatch-api.net/api/v1').json()
        self.api_hero_index = self.populate()

    def checkInHero(self,x):
        if x not in self.api_hero_index:
            errormsg = 'Hero not found : ' + x + '\n'
            errormsg += 'Please enter any of the following : \n'
            errormsg += '``` \n'
            for z in self.api_hero_index.keys():
                errormsg += str(z + '\n')
            errormsg += '```'
            return errormsg
        else:
            return 'OK'

    def getHeroData(self,x):
        return requests.get(self.api_hero_index[x]).json()

