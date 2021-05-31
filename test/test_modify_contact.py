from model.contact import Contact

def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="update Contact firstname", lastname="33333")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

#def test_modify_all(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname='test'))
#    app.contact.modify_first_contact(Contact(firstname="aaaaa", middlename="aaaaa", lastname="aaaaa", nickname="aaaaa", title="aaaaa",
#                company="aaaaa", address="aaaaa", home="aaaaa", mobile="aaaaa", work="aaaaa",
#                fax="aaaaa", email="aaaaa", email2="aaaaa", email3="aaaaa", homepage="aaaaa", bday="20",
#                bmonth="November", byear="2020", aday="20", amonth="September",
#                ayear="2020", address2="aaaaa", phone2="aaaaa", notes="aaaaa"))