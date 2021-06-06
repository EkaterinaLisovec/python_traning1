# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                      company="", address="", homephone="", mobilephone="", workphone="",
                      fax="", email="", email2="", email3="", homepage="", bday="15",
                      bmonth="September", byear="5555", aday="14", amonth="November",
                      ayear="6666", address2="", phone2="", notes="")] + [
            Contact(firstname=random_string("firstname",20), middlename=random_string("middlename",20), lastname=random_string("lastname",20),
            nickname=random_string("nickname",10), title=random_string("title",10), company=random_string("company",20),
            address=random_string("address",20), homephone=random_string("homephone",10),mobilephone=random_string("mobilephone",10),
            workphone=random_string("workphone",10), fax=random_string("fax",10), email=random_string("email",20),
            email2=random_string("email2",20), email3=random_string("email3",20), homepage=random_string("homepage",20),
            address2=random_string("address2",20), phone2=random_string("phone2",10), notes=random_string("notes",20))
    for i in range(2)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    # добавление новой группы в список
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)