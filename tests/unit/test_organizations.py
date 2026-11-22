
def test_create_organization(client):
    response = client.post(
        "/api/v1/organizations/",
        json={
            "name": "Test Organization",
            "slug": "test-organization",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Organization"
    assert data["slug"] == "test-organization"
    assert data["is_active"] is True


def test_list_organizations(client):
    client.post(
        "/api/v1/organizations/",
        json={
            "name": "Listing Organization",
            "slug": "listing-organization",
        },
    )

    response = client.get("/api/v1/organizations/")

    assert response.status_code == 200
    assert any(
        organization["slug"] == "listing-organization"
        for organization in response.json()
    )


def test_get_organization(client):
    create_response = client.post(
        "/api/v1/organizations/",
        json={
            "name": "Get Organization",
            "slug": "get-organization",
        },
    )

    organization_id = create_response.json()["id"]

    response = client.get(
        f"/api/v1/organizations/{organization_id}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == organization_id


def test_get_nonexistent_organization(client):
    response = client.get(
        "/api/v1/organizations/00000000-0000-0000-0000-000000000001"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Organization not found."


def test_duplicate_organization_slug(client):
    payload = {
        "name": "Duplicate Test",
        "slug": "duplicate-test",
    }

    first_response = client.post(
        "/api/v1/organizations/",
        json=payload,
    )

    second_response = client.post(
        "/api/v1/organizations/",
        json=payload,
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 409
