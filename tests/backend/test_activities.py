def test_get_activities(client):
    # Arrange & Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert "Chess Club" in data


def test_signup_and_unregister_flow(client):
    # Arrange
    activity = "Chess Club"
    email = "new_student@mergington.edu"

    # Act - signup
    signup_resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert signup succeeded
    assert signup_resp.status_code == 200
    assert f"Signed up {email} for {activity}" in signup_resp.json().get("message", "")

    # Act - unregister
    unregister_resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert unregister succeeded
    assert unregister_resp.status_code == 200
    assert "message" in unregister_resp.json()


def test_signup_existing_participant_returns_400(client):
    # Arrange - use an email already present in initial data
    activity = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": existing_email})

    # Assert
    assert resp.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    # Act
    resp = client.post("/activities/NoSuchActivity/signup", params={"email": "x@x.com"})

    # Assert
    assert resp.status_code == 404


def test_unregister_nonexistent_activity_returns_404(client):
    # Act
    resp = client.delete("/activities/NoSuchActivity/participants", params={"email": "x@x.com"})

    # Assert
    assert resp.status_code == 404


def test_unregister_not_signed_up_returns_404(client):
    # Arrange
    activity = "Chess Club"
    not_signed_up_email = "not_signed_up@mergington.edu"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": not_signed_up_email})

    # Assert
    assert resp.status_code == 404
