def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(update_middlename="3333333333333")
    app.session.logout()