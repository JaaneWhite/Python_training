def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()

def test_delete_all_contacs(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_all_contacts()
    app.session.logout()