import xlrd
import xlwt
import openpyxl
import xlrd
from xlutils.copy import copy


def readUsers(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    list =[]
    for i in range(0, worksheet.nrows):
        row = worksheet.row(i)
        for j in range(1, worksheet.ncols):
            list.append(worksheet.cell_value(i, j))
        print()
    return list   


def readCases(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    clist =[]
    for i in range(1, worksheet.nrows):
        row = worksheet.row(i)
        strappend =''
        for j in range(3, worksheet.ncols):
            if worksheet.cell_value(i, j) !='':
             strappend= strappend+worksheet.cell_value(i, j)+","
        
        clist.append(strappend)
        print(clist)
    return clist

def excelUpdate(resultstrclient):
    liststr=resultstrclient.split(':')
    excel=liststr[0]
    resultstr=liststr[1]
    caseid=int(liststr[2])
    wb = xlrd.open_workbook(excel)
    newb = copy(wb)
    wbsheet = newb.get_sheet(0)
    try:
     resultstrlist = resultstr.split(',')
    except Exception as ex:print(ex)
    wbsheet.write(caseid,0,resultstrlist[0])
    if len(resultstrlist)>1:
        try:
            wbsheet.write(caseid,1,resultstrlist[1])
            wbsheet.write(caseid,2,resultstrlist[2])
        except Exception as e: print(e)
    newb.save(excel)



