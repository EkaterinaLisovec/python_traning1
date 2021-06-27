from model.contact import Contact
import random
from random import randrange
import allure


def test_modify_firstname(app,db, check_ui):
    with allure.step('Check len of contact_list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname='test'))
    with allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Choose contact for update'):
        contact_old = random.choice(old_contacts)
        index = old_contacts.index(contact_old)
        contact = Contact(firstname="update Contact firstname", lastname="33333")
        contact.id = contact_old.id
    with allure.step('When I updated a contact %s to the list' % contact_old):
        app.contact.modify_contact_by_id(contact_old.id, contact)
    with allure.step('Then the new contact list is equal to the old list with the updated contact'):
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        new_contacts = map(app.contact.clean_contact, new_contacts)
        old_contacts = map(app.contact.clean_contact, old_contacts)
        old_contacts = list(old_contacts)
        old_contacts[index] = contact
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