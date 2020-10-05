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
        print("initialize...")
        for ele in self.req_types:
            self.matches[ele] = 0
        str_json = json.dumps(self.matches, indent=2)
        file1 = open(self.filename, "w")
        file1.write(str_json)
        file1.write("\n\n\n")
        file1.close()
        self.test_parse_json()
        for ele in self.req_types:
            print(ele, ";", self.matches[ele])
        str_json2 = json.dumps(self.matches, indent=2)
        self.append_file(str_json2)


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
                    s = ""
                    t_parent = False
                    t_key=False
                    t_val=False
                    try:
                        if parent.lower() == ele.lower():
                            t_parent, s = True, '\n\n\tmatch--> ' + ele + ',\t parent: ' + parent + '\n'
                        elif key.lower() == ele.lower():
                            t_key, s = True,  '\n\n\tmatch--> ' + ele + ',\t key: ' + key + '\n'
                        elif value.lower() == ele.lower():
                            t_val, s = True,  '\n\n\tmatch--> ' + ele + ',\t value: ' + value + '\n'
                        else: continue
                        print(s)
                    except:
                        pass

                    if t_parent or t_key or t_val:
                        self.append_file(str2)
                        self.matches[ele] = (self.matches[ele] + 1)

    def append_file(self, str):
        file1 = open(self.filename, "a")
        file1.write(str)
        file1.write("\n")
        file1.close()

    def split_list(self, parent, li):
        for i in li:
            if isinstance(i, dict):
                self.split_dict(parent, i)
