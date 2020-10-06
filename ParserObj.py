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
        file1.writelines(["search for=",str_json])
        file1.write("\n\n\n")
        file1.close()
        self.test_parse_json()
        for ele in self.req_types:
            print(ele, ";", self.matches[ele])


    def test_parse_json(self):
        with open(self.file_name) as f:
            data = json.load(f)
        self.split_dict("root", data)

    def split_dict(self, parent, di):
        for key, value in di.items():
            if isinstance(value, dict):
                self.split_dict(key, value)
            elif isinstance(value, list):
                self.split_list(key, value)
                continue
            else:
                for ele in self.req_types:
                    s = ""
                    t_parent = False
                    t_key=False
                    t_val=False
                    matched = None
                    try:
                        if parent.lower() == ele.lower():
                            t_parent, matched, s = True, parent.lower(), '\n\n\tmatch--> ' + ele + ',\t parent: ' + parent + '\n'
                        elif key.lower() == ele.lower():
                            t_key, matched, s = True, key.lower(), '\n\n\tmatch--> ' + ele + ',\t key: ' + key + '\n'
                        elif value.lower() == ele.lower():
                            t_val, matched, s = True, value.lower(), '\n\n\tmatch--> ' + ele + ',\t value: ' + value + '\n'
                        else: continue
                        print(s)
                    except:
                        pass
                    if t_parent:
                        self.append_file(json.dumps(di, indent=4))
                        self.matches[ele] = (self.matches[ele] + 1)
                    elif t_key or t_val:
                        strX = self.unpack_json_val(di, parent, matched)
                        if len(strX) > 0:
                            self.append_file(json.dumps(strX, indent=4))
                            self.matches[ele] = (self.matches[ele] + 1)


    def unpack_json_val(self, di, parent, matched):
        strX = {}
        strX['type'] = matched
        for ele2 in self.req_fields:
            for key, val in di.items():
                if key.lower() == ele2.lower():
                    strX[ele2] = val
                    break
        return strX

    def append_file(self, str):
        file1 = open(self.filename, "a")
        file1.write(str)
        file1.write("\n")
        file1.close()

    def split_list(self, parent, li):
        for i in li:
            if isinstance(i, dict):
                self.split_dict(parent, i)


    def summary_file(self):
        file1=open("summary.json")
        str_json = json.dumps(self.matches, indent=2)
        file1.writelines(str_json)
        file1.close()