from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_basic_round_and_guess():
    r = client.post('/round', json={'min':2,'max':5,'size':6,'seed':123})
    assert r.status_code == 200
    data = r.json()
    rid = data['round_id']
    product = data['product']
    nums = data['numbers']

    # brute force a correct pair from returned numbers
    found = None
    for a in nums:
        for b in nums:
            if a*b == product:
                found = (a,b); break
        if found: break
    assert found is not None

    g = client.post('/guess', json={'round_id': rid, 'a': found[0], 'b': found[1]})
    assert g.status_code == 200
    assert g.json()['correct'] is True

    s = client.get(f'/status/{rid}')
    assert s.status_code == 200
    st = s.json()
    assert st['used_pairs'] >= 1
