
## 요구분석
# - dbf edit / 일괄 칼럼 드랍 PNU,JIBUN,BCHK / JIMOK 있을 경우 - drop  
# - https://pythonhosted.org/dbf/dbf-module.html
## 의존성 로드 DBF module
import datetime
import dbf
import os

##하위 경로 DBF 검색
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname,filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext=='.dbf':
                    print(full_filename)
                    return(full_filename) 
    except PermissionError:
        pass

DBF_FILE_LIST=search("./")





##하위 경로 DBF 로드
for DBF in DBF_FILE_LIST:
    table = dbf.Table(DBF)
    table.open()
    ### 필드 드립 포문 pql_drop / delete_fields(dead_fields) , https://github.com/ethanfurman/dbf/blob/master/dbf/__init__.py
    ###     지목 존재 - 지목 확인 후 지목 값 변경
    ###     지목 변경 - 지번에 합치기

##하위 경로 DBF에 대하여 일괄 데이터 슬라이싱


##일괄 저장
for record in custom:
    dbf.write(record, name=record.name.upper())