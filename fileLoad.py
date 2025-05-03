import json
class LoadData:
    def loadData(self):
        with open('data/people.json','r') as f:
            data = json.load(f)
            return data
