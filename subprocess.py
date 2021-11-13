import sys
import subprocess
from datetime import date, datetime
import datetime as dt
import time, datetime

start = time.time()
now = dt.datetime.now()
print('Início = ',now.strftime("%d/%m/%Y, %H:%M:%S"))

arquivos = ['1.py','2.py','3.py','4.py']
processos = []

for arquivo in arquivos:
    processo = subprocess.Popen([sys.executable, arquivo])
    processos.append(processo)

# neste ponto todos os scripts estão rodando em background ao mesmo tempo. 
# Vamos esperar todos eles terminarem:

for processo in processos:
    processo.wait()

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))