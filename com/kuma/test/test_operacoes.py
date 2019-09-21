import pytest
from com.kuma.calcula_parcela import valorPagamento
from com.kuma.convertehora import converteHora

def test_retornarNone():
	operacao = converteHora(24, 0)
	assert operacao == None, "Deveria ser None"
	
def test_retornarMeiodia():
	operacao = converteHora(0, 10)
	assert operacao == "12:10 AM", "Deveria ser 12:10 AM"

def test_retornarOnze():
	operacao = converteHora(9, 10)
	assert operacao == "09:10 AM", "Deveria ser 9:10 AM"
	
def test_retornarNone():
	operacao = converteHora(13, 10)
	assert operacao == "01:10 PM", "Deveria ser 1:10 AM"
    


def test_doisdiasAtraso():
	operacao = valorPagamento(100,2)
	assert operacao == 105, "Deveria ser 105"

def test_valorZero():
	operacao = valorPagamento(-1,0)
	assert operacao == None, "Deveria ser 0"
	
	
def test_semAtraso():
	operacao = valorPagamento(100,0)
	assert operacao == 100, "Deveria ser 100"

