# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1111", middlename="22222", lastname="33333", nickname="44444", title="5555",
                      company="66666", address="77777", homephone="8888", mobilephone="9999", workphone="666",
                      fax="11111", email="22222", email2="33333", email3="444444", homepage="5555", bday="15",
                      bmonth="September", byear="5555", aday="14", amonth="November",
                      ayear="6666", address2="55555", phone2="5555", notes="555555")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    # добавление новой группы в список
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)