import pytest
from com.kuma.calcula_parcela import valorPagamento

def test_doisdiasAtraso():
	operacao = valorPagamento(100,2)
	assert operacao == 105, "Deveria ser 105"

def test_valorZero():
	operacao = valorPagamento(-1,0)
	assert operacao == None, "Deveria ser 0"
	
	
def test_semAtraso():
	operacao = valorPagamento(100,0)
	assert operacao == 100, "Deveria ser 100"