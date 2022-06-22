from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def home_cep(request):
    return render(request, 'home_cep.html')

def consulta_cep(request):
    if request.method != 'POST':
        return redirect('home_cep')
    else:
        cep = request.POST.get('cep')
        if not cep.isnumeric():
            messages.add_message(request, messages.ERROR, 'CEP informado inválido, precisa ser apenas números (sem pontos, traços ou caracteres especiais)')
            return redirect('home_cep')
        if len(cep) != 8:
            messages.add_message(request, messages.ERROR, 'CEP informado inválido, precisa ter 8 digitos')
            return redirect('home_cep')
        else:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
            if len(response) == 1:
                messages.add_message(request, messages.ERROR, 'CEP inválido ou não foi encontrado na base de dados, verifique')
                return redirect('home_cep')
            else:
                return render(request, 'consulta_cep.html', {'response':response})
def consulta_rua(request):
    estado = request.POST.get('estado')
    cidade = request.POST.get('cidade')
    rua = request.POST.get('rua')
    if not cidade or not rua:
        messages.add_message(request, messages.ERROR, 'Nenhum campo pode ser vazio')
        return redirect('home_cep')
    if len(cidade) < 3 or len(rua) < 3:
        messages.add_message(request, messages.ERROR, 'Cidade ou rua inválidos, precisam ter ao menos 3 caracteres cada pra consulta')
        return redirect('home_cep')
    else:
        response = requests.get(f'https://viacep.com.br/ws/{estado}/{cidade}/{rua}/json/').json()
        if len(response) == 0:
            messages.add_message(request, messages.ERROR, f'Rua {rua} na cidade {cidade} no estado {estado} não localizada, verifique os dados digitados')
            return redirect('home_cep')
        else:
            total_ruas = len(response)
            return render(request, 'consulta_rua.html', {'response':response, 'rua':rua, 'cidade':cidade, 'estado':estado, 'total_ruas':total_ruas})

def detalhes(request, cep):
    cep = cep.replace('-', '')
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    if len(response) == 1:
        messages.add_message(request, messages.ERROR, 'CEP inválido ou não foi encontrado na base de dados, verifique')
        return redirect('home_cep')
    else:
        return render(request, 'consulta_cep.html', {'response':response})
