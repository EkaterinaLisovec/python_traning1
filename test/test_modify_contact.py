from model.contact import Contact

def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    app.contact.modify_first_contact(Contact(firstname='update Contact firstname'))

def test_modify_all(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test'))
    app.contact.modify_first_contact(Contact(firstname="aaaaa", middlename="aaaaa", lastname="aaaaa", nickname="aaaaa", title="aaaaa",
                company="aaaaa", address="aaaaa", home="aaaaa", mobile="aaaaa", work="aaaaa",
                fax="aaaaa", email="aaaaa", email2="aaaaa", email3="aaaaa", homepage="aaaaa", bday="20",
                bmonth="November", byear="2020", aday="20", amonth="September",
                ayear="2020", address2="aaaaa", phone2="aaaaa", notes="aaaaa"))