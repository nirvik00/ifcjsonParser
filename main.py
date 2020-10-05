import time
from ParserObj import ParserObj

def f8():
    test_data, small_data, pp_data, duplex_data = "test.json", "data1.json", "data2.json", "duplex_data.json"
    req_types = ["ifcDoor", "ifcproject", "ifcsite", "ifcbuilding"]
    req_types += ["ifcwall", "ownerHistory", "relatedElements"]
    req_fields = ["globalid", "name", "description", "relatedelements", "isdecomposedby"]
    p = ParserObj(test_data, req_types, req_fields)

if __name__ == '__main__':
    start_time=time.time()
    print('running program...')
    f8()
    end_time = time.time()
    print('...end program')
    print('time in seconds: %s' %(end_time-start_time))


