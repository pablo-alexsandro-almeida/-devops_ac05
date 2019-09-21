import pytest

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
	
