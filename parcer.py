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

# class SearchInfo:
#     def __init__(self):
