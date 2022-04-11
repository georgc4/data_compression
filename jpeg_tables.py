import csv
with open('ac.csv') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj, delimiter = ' ')
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(map(tuple,csv_reader))
print(list_of_rows)
ac_dict = dict()
for row in list_of_rows:
    run,category = int(row[0]), int(row[1])
    ac_code_length,ac_code = int(row[2]), row[3]
class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range): # or xrange in Python 2
            for key in self:
                if abs(item) in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item) # or super(RangeDict, self) for Python 2

cat = RangeDict({range(0,1):0, range(1,2):1, range(2,4):2,range(4,8):3, range(8,16):4, range(16,32):5,
        range(32,64):6, range(64,128):7, range(128,256):8, range(256,512):9,range(512,1024):10, range(1024,2048):11, range(2048,4096):12,
        range(4096,8192):13, range(8192,16384):14, range(16384,32768):15})


dc_code = {0:(2,'00'),1:(3,'010'),2:(3,'011'),3:(3,'100'),4:(3,'101'),5:(3,'110'),6:(4,'1110'),7:(5,'11110'),8:(6,'111110'),9:(7,'1111110'),10:(8,'11111110'),11:(9,'111111110')}

