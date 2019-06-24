import pandas as pd
import trychecking
import perplexity
xls = pd.ExcelFile("DataSet.xlsx")

sheetX = xls.parse(0) #2 is the sheet number

var1 = sheetX['essay']

#for i in var1:
     # print(i)
      #trychecking.OnClick(i)
perplexity.RunThis(var1[0])
