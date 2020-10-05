import json

class ParserObj(object):
    def __init__(self, filename, req_types, req_fields):
        self.file_name = filename
        self.element_dict = {}
        self.element_list = []
        self.req_types = req_types
        self.req_fields = req_fields
        self.matches = {}
        self.filename = "SampleTest2.json"
        self.initialize()

    def initialize(self):
        for ele in self.req_types:
            self.matches[ele] = 0
        str_json = json.dumps(self.matches, indent=2)
        file1 = open(self.filename, "w")
        file1.write(str_json)
        file1.write("\n\n\n")
        file1.close()
        self.test_parse_json()

    def test_parse_json(self):
        with open(self.file_name) as f:
            data = json.load(f)
        self.split_dict("root", data)

    def split_dict(self, parent, di):
        str2 = json.dumps(di, indent=4)
        for key, value in di.items():
            if isinstance(value, dict):
                self.split_dict(key, value)
            elif isinstance(value, list):
                self.split_list(key, value)
            else:
                for ele in self.req_types:
                    t = False
                    try:
                        if parent.lower() == ele.lower() or \
                                key.lower() == ele.lower() or \
                                value.lower() == ele.lower():
                            t = True
                    except:
                        pass
                    if t:
                        s = '\n\n\tmatch--> ' + ele + ',\t parent: ' + parent + '\n'
                        print(self.req_fields)
                        self.append_file(str2)
                        self.matches[ele] = (self.matches[ele] + 1)

    def append_file(self, str):
        file1 = open(self.filename, "a")
        file1.write(str)
        file1.close()

    def split_list(self, parent, li):
        for i in li:
            if isinstance(i, dict):
                self.split_dict(parent, i)
