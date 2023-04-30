import requests


class Info:
    def __init__(self, agent_name, map_name, side_name, vid_ref):
        self.agent_name = agent_name
        self.map_name = map_name
        self.side_name = side_name
        self.vid_ref = vid_ref

    def get_ref(self):
        return self.vid_ref

    def get_agent(self):
        return self.agent_name

    def get_map(self):
        return self.map_name

    def get_side(self):
        return self.side_name

    def set_ref(self, ref):
        self.vid_ref = ref

    def set_agent(self, agent):
        self.agent_name = agent

    def set_map(self, map):
        self.map_name = map

    def set_side(self, side):
        self.side_name = side


class ValorantInfo:

    def __init__(self):
        self._maps = None
        self._heroes = None
        self._sides = ['Атака', 'Защита', 'Обе']

    def maps(self):
        if self._maps is None:
            page = requests.get("https://playvalorant.com/page-data/ru-ru/maps/page-data.json")
            content = page.json()
            self._maps = [game_map['title'] for game_map
                          in content['result']['data']['allContentstackMaps']['nodes'][0]['related_content']]
        return self._maps

    def heroes(self):
        if self._heroes is None:
            page = requests.get("https://playvalorant.com/page-data/ru-ru/agents/page-data.json")
            content = page.json()
            self._heroes = [agent['related_content'][0]['title'] for agent
                          in content['result']['data']['allContentstackAgentList']['nodes'][0]['agent_list']]
        return self._heroes

    def sides(self):
        return self._sides
