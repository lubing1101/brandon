#!/usr/local/python/bin/python
# -*- coding: utf-8 -*- 
import xdrlib ,sys ,time
import xlrd
import xlwt
import linecache
import urllib
#sys.setdefaultencoding('utf-8')
nowtime = time.strftime('%Y-%m-%d')
oldtime = time.strftime('%Y-%m-%d',time.localtime(time.time()-1*24*60*60))

workfile = "work_order_exam"+oldtime+".xls"
def open_excel(file = workfile):
     try:
         data = xlrd.open_workbook(file)
         return data
     except Exception,e:
         print str(e)
 
def excel_table_byindex(file= workfile,colnameindex=0,by_index=0):
     data = open_excel(file)
     outfile = open('excelprint.txt','w')
     table = data.sheets()[by_index]
     nrows = table.nrows 
     ncols = table.ncols 
     colnames =  table.row_values(colnameindex)
     list = []
     for rownum in (2,6,10):
          row = table.row_values(rownum)	  
          print >> outfile,row
	  #print >> outfile,row.decode('unicode').encode('utf-8')
	  if row:
                app = {}
                for i in range(len(colnames)):
	             
                     app[colnames[i]] = row[i]
                list.append(app)
     return list

def main():
     tables = excel_table_byindex()
     for row in tables:
          return row


if __name__=="__main__":
     main()
