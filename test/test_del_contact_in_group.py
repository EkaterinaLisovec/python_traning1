# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_in_group(app):
    #проверка наличия групп, если их нет, то добавляем
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name='test'))
        groups = db.get_group_list()
    #сначала проверим, что существует хоть один несвободный контакт
    if len(check_not_free_contact(groups)) == 0:
        app.contact.create(Contact(firstname='test'))
        new_contacts = db.get_contact_list()
        contact = max(new_contacts, key=Contact.id_or_max)
        app.contact.add_contact_in_group(contact.id, groups[0].id)
    not_free_contacts = check_not_free_contact(groups)
    not_free_contact_in_group = not_free_contacts[0]
    group_id = not_free_contact_in_group[1]
    not_free_contacts = not_free_contact_in_group[0]
    not_free_contact = not_free_contacts[0]
    app.contact.del_contact_in_group(not_free_contact.id, group_id)
    # проверка удаления контакта из группы
    contacts_in_group = (db.get_contacts_in_group(Group(id=group_id)))[0]
    list_of_id=[]
    for item in contacts_in_group:
        list_of_id.append(item.id)
    assert not_free_contact.id not in list_of_id


def check_not_free_contact(groups):
    not_free_contacts = []
    for i in range(0, len(groups)):
          group = groups[i]
          if db.get_contacts_in_group(group)[0] != []:
              not_free_contacts.append(db.get_contacts_in_group(group))
    return not_free_contacts