from src.database import get_user, save_user, delete_user

def test_get_user():
    result = get_user(1)
    assert result["id"] == 1

def test_get_user_invalid():
    assert get_user(-1) is None

def test_save_user():
    assert save_user({"name": "Alice"}) == True

def test_delete_user():
    assert delete_user(1) == True
