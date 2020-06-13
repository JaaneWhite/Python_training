from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="Helen", middlename="Mark", lastname="Rozenblum", nickname="HMR",
                title="Mini Boss", company="OOO Ltd", address="123456, Hongkong, Hongkong", home="123789456",
                mobile="1234567891", work="102356879", fax="1000234658",
                email="helen@dot.com", email2="helen@mail.ru", email3="helen@gmail.com",
                homepage="helen.net", bmonth="April", bday="28", byear="1995", aday="20",
                amonth="May", ayear="2018", address2="123456, Hongkong, Hongkon", phone2="1111111111",
                notes="ohnononono", photo="D:\Kakurenbo1.jpg"))

    app.contact.return_homepage()
    app.session.logout()