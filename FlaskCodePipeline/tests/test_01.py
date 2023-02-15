
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert "Hello World!" in res.get_data(as_text=True)