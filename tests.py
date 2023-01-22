from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_query_person_graphql():
  query = """{
    person {
      name
      address {
        street
        number
        state
      }
    }
  }"""

  response = client.get('/graphql')
  assert response.status_code == 200
