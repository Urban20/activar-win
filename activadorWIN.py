import platform,os,time
from art import *

codigos= {
    'Home': 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
    'HomeN': '3KHY7-WNT83-DGQKR-F7HPR-844BM',
    'CoreSingleLanguage': '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH',
    'HomeCountrySpecific':'PVMJN-6DFY6-9CCP6-7BKTT-D3WVR',
    'Professional': 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
    'ProfessionalN': 'MH37W-N47XK-V7XM9-C7227-GCQG9',
    'Enterprise': 'NPPR9-FWDCX-D2C8J-H872K-2YT43',
    'EnterpriseN': 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4',
    'Education': 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
    'EducationN': '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ',
    'EnterpriseLTSB': 'WNMTR-4C88C-JK8YV-HQ7T2-76DF9',
    'EnterpriseLTSBN': '2F77B-TNFGY-69QQF-B8YKP-D69TJ'
    }

tprint('URB@N')
print('URB@N')

def comando(codigo,version):
    print(f'windows/ version:{version}')
    os.system(f'slmgr /ipk {codigo}')
    time.sleep(5)
    os.system('slmgr /skms kms.digiboy.ir')
    time.sleep(5)
    os.system('slmgr /ato')
    
if platform.system() == 'Windows':
    try:
        version= platform.win32_edition()
        codigo = codigos[version]
        comando(codigo,version)
    except:
        print('error')