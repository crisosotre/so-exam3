import pytest
from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'porcentaje_cpu', return_value=100)
  response = client.get('/CPU')
  assert response.data.decode('utf-8') == '{"Porcentaje CPU": 100}'
  assert response.status_code == 200

def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'ram_disponible', return_value=20)
  response = client.get('/RAM')
  assert response.data.decode('utf-8') == '{"Memoria Disponible": 20}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'espacio_disco_disponible', return_value=30)
  response = client.get('/DISCO')
  assert response.data.decode('utf-8') == '{"Espacio Libre Disco": 30}'
  assert response.status_code == 200
