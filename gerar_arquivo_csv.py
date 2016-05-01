__author__ = 'ceb'

import csv
import os
from carro_service import CarroService

unidade='c'
diretorioBase=''

if os.name == 'nt':
    diretorioBase=unidade+':'
else:
    diretorioBase=os.getenv("HOME")

carroService = CarroService()

listaModelosCarros = carroService.findAll()

caminhoAbsoluto = diretorioBase + os.sep + 'csv' + os.sep
if not os.path.exists(caminhoAbsoluto):
    os.makedirs(caminhoAbsoluto)

arquivoOutput = caminhoAbsoluto + 'python_gerando_arquivo.csv'

listaParaGerarCsv = []
for dictCarro in listaModelosCarros:
    listaInterna = []
    listaInterna.append(dictCarro['marca'])
    listaInterna.append(dictCarro['modelo'])
    listaInterna.append(dictCarro['ano'])

    listaParaGerarCsv.append(listaInterna)

with open(arquivoOutput, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Marca', 'Modelo', 'Ano'])
    for linha in listaParaGerarCsv:
        spamwriter.writerow(linha)

print 'Arquivo gerado no diretorio: ' + arquivoOutput
