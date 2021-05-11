# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="1111", middlename="22222", lastname="33333", nickname="44444", title="5555",
                company="66666", address="77777", home="8888", mobile="9999", work="00000",
                fax="11111", email="22222", email2="33333", email3="444444", homepage="5555", bday="15",
                bmonth="September", byear="5555", aday="14", amonth="November",
                ayear="6666", address2="55555", phone2="5555", notes="555555"))