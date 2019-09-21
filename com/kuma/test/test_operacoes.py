import pytest
from com.kuma.calcula_parcela import valorPagamento
from com.kuma.contaCorrente import ContaCorrente

def test_deposito():
	contaCorrente = ContaCorrente(1222, "pablo")
	contaCorrente.deposito(100)
	assert contaCorrente.saldo == 100, "Valor e 100"
	
def test_alterarNome():
	contaCorrente = ContaCorrente(1222, "pablo")
	contaCorrente.alterarNome("julio")
	assert contaCorrente.nomeCorrentista == "julio", " Era Pablo"

def test_saque():
	contaCorrente = ContaCorrente(1222, "pablo")
	contaCorrente.saque(100)
	assert contaCorrente.saldo == -100, "Valor e 100"
	

def test_doisdiasAtraso():
	operacao = valorPagamento(100,2)
	assert operacao == 105, "Deveria ser 105"

def test_valorZero():
	operacao = valorPagamento(-1,0)
	assert operacao == None, "Deveria ser 0"
	
	
def test_semAtraso():
	operacao = valorPagamento(100,0)
	assert operacao == 100, "Deveria ser 100"

