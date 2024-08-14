import platform,os,time
from art import *

codigos= {
    'Home': 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
    'Home N': '3KHY7-WNT83-DGQKR-F7HPR-844BM',
    'Home Single Language': '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH',
    'Home Country Specific':'PVMJN-6DFY6-9CCP6-7BKTT-D3WVR',
    'Professional': 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
    'Professional N': 'MH37W-N47XK-V7XM9-C7227-GCQG9',
    'Enterprise': 'NPPR9-FWDCX-D2C8J-H872K-2YT43',
    'Enterprise N': 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4',
    'Education': 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
    'Education N': '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ',
    'Enterprise 2015 LTSB': 'WNMTR-4C88C-JK8YV-HQ7T2-76DF9',
    'Enterprise 2015 LTSB N': '2F77B-TNFGY-69QQF-B8YKP-D69TJ'
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
        codigo = codigos.get(version)
        comando(codigo,version)
    except:
        print('error')