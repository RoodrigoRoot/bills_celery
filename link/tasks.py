from celery import shared_task
from ftplib import FTP

@shared_task
def get_bills_moth():
    #month = "manual_en.pdf" 
    #ftp = FTP("demo.wftpserver.com")
    #ftp.login("demo-user", "demo-user")
    #ftp.cwd("download")
    #ftp.retrbinary("RETR " + month ,open(month, 'wb').write)
    print("Factura descargada")
    return 0