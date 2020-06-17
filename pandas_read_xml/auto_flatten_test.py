import pandas as pd
import pandas_read_xml as pdx
from pandas_read_xml import auto_separate_tables


file_path = 'data_science_learning/BOM&Wire analysis/ELZ_TAB016161D_KSK_L0L_160620.xml'
root_key_list = ['HarnessContainer', 'Harness', 'Connectors']
key_columns = ['Connector', 'ConnectorModuleRefs|ConnectorModuleRef']

df = pdx.read_xml(file_path, root_key_list)
data = df.pipe(auto_separate_tables, key_columns)
# data.to_excel('data_science_learning/pandas_read_xml/apc200219_new.xlsx')
print(data.keys())