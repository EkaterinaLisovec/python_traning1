from model.contact import Contact
from random import randrange

def test_modify_firstname(app,db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test'))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="update Contact firstname", lastname="33333")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    new_contacts = map(app.contact.clean_contact, new_contacts)
    old_contacts = map(app.contact.clean_contact, old_contacts)
    old_contacts = list(old_contacts)
    old_contacts[index] = contact
    #old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_modify_all(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname='test'))
#    app.contact.modify_first_contact(Contact(firstname="aaaaa", middlename="aaaaa", lastname="aaaaa", nickname="aaaaa", title="aaaaa",
#                company="aaaaa", address="aaaaa", home="aaaaa", mobile="aaaaa", work="aaaaa",
#                fax="aaaaa", email="aaaaa", email2="aaaaa", email3="aaaaa", homepage="aaaaa", bday="20",
#                bmonth="November", byear="2020", aday="20", amonth="September",
#                ayear="2020", address2="aaaaa", phone2="aaaaa", notes="aaaaa"))