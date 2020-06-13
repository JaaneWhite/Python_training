# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        # add new contact
        app.contact.create_contact(Contact(firstname="Yadviga",middlename="Innokentievna",lastname="Shulz",nickname="YIS",
                                        title="Mega Boss",company="WOW Ltd",address="111000, Sheeptown, USA",home="+7-999-111-2222",
                                        mobile="+7-999-111-3333",work="+7-888-123-4562",fax="+7-999-111-2222",
                                        email="yadviga@dot.com",email2="yadviga@mail.ru",email3="yadviga@gmail.com",
                                        homepage="yadviga.net",bmonth="October",bday="10",byear="1999",aday="16",
                                        amonth="December",ayear="2005",address2="111000, Sheeptown, USA",phone2="Sweet Home",
                                        notes="bla bla bla",photo="D:\Kakurenbo1.jpg"))

        app.contact.return_homepage()
        app.session.logout()
