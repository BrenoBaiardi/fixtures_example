# contents of test_module.py with source code and the test
import random
import requests



def test_get_fake_random(monkeypatch):
    def get_fake_random():
        return 0

    monkeypatch.setattr(random, "random", get_fake_random)

    x = random.random()
    assert x == 0

def test_fake_pi(monkeypatch):
    monkeypatch.setattr(random, "TWOPI", 1)
    assert random.TWOPI == 1


def minha_resposta_fake(url: str):
    return "valor_fake"

# O Código abaixo faz o monkey patch mas não é uma fixture,
# só será uma fixture quando for marcado com pytest.fixture
# ao ser transformado em fixture, poderá ser utilizado em varios testes
# VERIFICAR SE O MONKEYPATCH É DESFEITO AO FIM DA FIXTURE
def test_fake_pi(monkeypatch):
    monkeypatch.setattr(requests, "get", minha_resposta_fake)
    assert requests.get("https://reqres.in/") == "valor_fake"
