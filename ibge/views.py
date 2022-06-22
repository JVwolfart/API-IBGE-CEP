from django.shortcuts import render, redirect
import requests
from django.contrib import messages
# Create your views here.



def index_ibge(request):
    return render(request, 'index_ibge.html')

def busca(request):
    nome = request.GET.get('nome').title()
    if not nome:
        messages.add_message(request, messages.ERROR, 'Nenhum nome informado')
        return redirect('home')
    else:
        url = 'http://servicodados.ibge.gov.br/api/v2/censos/nomes/'
        frequencia = []
        response = requests.get(f'{url}{nome}').json()
        if response == []:
            messages.add_message(request, messages.ERROR, 'Nome não encontrado na base de dados')
            return redirect('home')

        for r in response[0]['res']:
            frequencia.append(r)
        
        for f in frequencia:
            f['periodo'] = f['periodo'].replace('[', '').replace(']', '').replace(',', ' =>')
            f['frequencia'] = str(f['frequencia'])
            if len(f['frequencia']) > 3:
                f['frequencia'] = f['frequencia'][:-3] + '.' + f['frequencia'][len(f['frequencia'])-3:]
                if len(f['frequencia']) > 7:
                    f['frequencia'] = f['frequencia'][:-7] + '.' + f['frequencia'][len(f['frequencia'])-7:]
                    

            

        return render(request, 'frequencia.html', {'nome':nome, 'frequencia':frequencia})

def ranking(request):
    response = requests.get('http://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/').json()
    ranking = []
    for f in response[0]['res']:
        ranking.append(f)
        f['frequencia'] = str(f['frequencia'])
        if len(f['frequencia']) > 3:
            f['frequencia'] = f['frequencia'][:-3] + '.' + f['frequencia'][len(f['frequencia'])-3:]
            if len(f['frequencia']) > 7:
                f['frequencia'] = f['frequencia'][:-7] + '.' + f['frequencia'][len(f['frequencia'])-7:]
                
    return render(request, 'ranking.html', {'ranking':ranking})

def ranking_m(request):
    response = requests.get('http://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M').json()
    ranking = []
    for f in response[0]['res']:
        ranking.append(f)
        f['frequencia'] = str(f['frequencia'])
        if len(f['frequencia']) > 3:
            f['frequencia'] = f['frequencia'][:-3] + '.' + f['frequencia'][len(f['frequencia'])-3:]
            if len(f['frequencia']) > 7:
                f['frequencia'] = f['frequencia'][:-7] + '.' + f['frequencia'][len(f['frequencia'])-7:]
                
    return render(request, 'ranking.html', {'ranking':ranking})

def ranking_f(request):
    response = requests.get('http://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=F').json()
    ranking = []
    for f in response[0]['res']:
        ranking.append(f)
        f['frequencia'] = str(f['frequencia'])
        if len(f['frequencia']) > 3:
            f['frequencia'] = f['frequencia'][:-3] + '.' + f['frequencia'][len(f['frequencia'])-3:]
            if len(f['frequencia']) > 7:
                f['frequencia'] = f['frequencia'][:-7] + '.' + f['frequencia'][len(f['frequencia'])-7:]
                
    return render(request, 'ranking.html', {'ranking':ranking})

def ranking_decada(request):
    decada = request.GET.get('decada')
    response = requests.get(f'http://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada={decada}').json()
    ranking = []
    for f in response[0]['res']:
        ranking.append(f)
        f['frequencia'] = str(f['frequencia'])
        if len(f['frequencia']) > 3:
            f['frequencia'] = f['frequencia'][:-3] + '.' + f['frequencia'][len(f['frequencia'])-3:]
            if len(f['frequencia']) > 7:
                f['frequencia'] = f['frequencia'][:-7] + '.' + f['frequencia'][len(f['frequencia'])-7:]
                
    return render(request, 'ranking_decada.html', {'ranking':ranking, 'decada':decada})

def curiosidades(request):
    return render(request, 'curiosidades.html')