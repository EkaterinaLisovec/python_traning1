import re
from model.contact import Contact
from random import randrange

def test_details_on_home_page(app, db):
    contacts_list_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_list_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_list_ui) == len(contacts_list_db)
    for i in range(0, len(contacts_list_db)):
        contact_from_home_page = contacts_list_ui[i]
        contact_list_db = contacts_list_db[i]
        assert contact_from_home_page.firstname == contact_list_db.firstname
        assert contact_from_home_page.lastname == contact_list_db.lastname
        assert contact_from_home_page.address == contact_list_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_list_db)
        assert contact_from_home_page.all_emeils_from_home_page == merge_emeils_like_on_home_page(
            contact_list_db)
    #index = randrange(len(contacts_list))
    #contact_from_home_page = app.contact.get_contact_list()[index]
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    #assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    #assert contact_from_home_page.address == contact_from_edit_page.address
    #assert contact_from_home_page.all_emeils_from_home_page == merge_emeils_like_on_home_page(contact_from_edit_page)

# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def clear_for_emeil(s):
    return re.sub("[()-]", "", s)

def merge_phones_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != "",
                    map(lambda x: clear(x),
                        filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))

def merge_emeils_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != "",
                    map(lambda x: clear_for_emeil(x),
                        filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))