import os
import dbf
DBF_FILE_LIST = []
##하위 경로 DBF 검색
filenames = os.listdir('./')
for filename in filenames:
    full_filename = os.path.join('./',filename)
    if os.path.isdir(full_filename):
        search(full_filename)
    else:
        ext = os.path.splitext(full_filename)[-1]
        if ext=='.dbf':
            print(filename)
            DBF_FILE_LIST.append(filename)

print(DBF_FILE_LIST)

table = dbf.Table('77-2.dbf')
table.open(mode=dbf.READ_WRITE)
t=dbf.get_fields('77-2.dbf')
print(t)

for DBF in DBF_FILE_LIST:
    print('getting',DBF)
    table=dbf.Table(DBF)
    table.open(mode=dbf.READ_WRITE)
    t=dbf.get_fields(DBF)
    print(t)
    
    