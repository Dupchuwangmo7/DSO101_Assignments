import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ──────────────────────────────────────────────
# Basic arithmetic checks (no HTTP needed)
# ──────────────────────────────────────────────

def test_basic_math():
    """Simple sanity check — 1 + 1 must equal 2."""
    assert 1 + 1 == 2


def test_multiplication_math():
    """3 × 4 must equal 12."""
    assert 3 * 4 == 12


# ──────────────────────────────────────────────
# Home route
# ──────────────────────────────────────────────

def test_home_status_code(client):
    """GET / returns HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_json(client):
    """GET / returns a JSON body."""
    response = client.get("/")
    data = response.get_json()
    assert data is not None


def test_home_message(client):
    """GET / response contains the expected message key."""
    response = client.get("/")
    data = response.get_json()
    assert "message" in data


def test_home_status_field(client):
    """GET / response reports status as 'running'."""
    response = client.get("/")
    data = response.get_json()
    assert data["status"] == "running"


# ──────────────────────────────────────────────
# Health-check route
# ──────────────────────────────────────────────

def test_health_status_code(client):
    """GET /health returns HTTP 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_body(client):
    """GET /health returns {'status': 'healthy'}."""
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "healthy"


# ──────────────────────────────────────────────
# Addition route
# ──────────────────────────────────────────────

def test_add_two_numbers(client):
    """GET /add/3/4 returns result 7."""
    response = client.get("/add/3/4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 7


def test_add_zero(client):
    """Adding 0 to any number returns that number."""
    response = client.get("/add/10/0")
    data = response.get_json()
    assert data["result"] == 10


def test_add_large_numbers(client):
    """Addition works for larger integers."""
    response = client.get("/add/1000/2000")
    data = response.get_json()
    assert data["result"] == 3000


# ──────────────────────────────────────────────
# Multiplication route
# ──────────────────────────────────────────────

def test_multiply_two_numbers(client):
    """GET /multiply/3/4 returns result 12."""
    response = client.get("/multiply/3/4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 12


def test_multiply_by_zero(client):
    """Multiplying any number by 0 returns 0."""
    response = client.get("/multiply/99/0")
    data = response.get_json()
    assert data["result"] == 0


def test_multiply_by_one(client):
    """Multiplying any number by 1 returns the same number."""
    response = client.get("/multiply/7/1")
    data = response.get_json()
    assert data["result"] == 7
