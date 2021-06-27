# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import allure

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_in_group(app):
    with allure.step('Check len of group_list'):
        #проверка наличия групп, если их нет, то добавляем
        groups = db.get_group_list()
        if len(groups) == 0:
            app.group.create(Group(name='test'))
            groups = db.get_group_list()
    with allure.step('Check free_contact'):
        #проверка наличия контактов, не добавленных в группы
        if len(check_free_contact(groups)) == 0:
            app.contact.create(Contact(firstname='test'))
    with allure.step('Find free_contact'):
        free_contacts = check_free_contact(groups)
        free_contact_in_group = free_contacts[0]
        group_id = free_contact_in_group[1]
        free_contacts = free_contact_in_group[0]
        free_contact = free_contacts[0]
    with allure.step('Add_contact_in_group'):
        app.contact.add_contact_in_group(free_contact.id, group_id)
    #group = db.get_group(Group(id=group_id))
    with allure.step('Check Adding contact in group'):
        #проверка добаления контакта в группу
        contacts_in_group = db.get_contacts_in_group(Group(id=group_id))[0]
        list_of_id=[]
        for item in contacts_in_group:
            list_of_id.append(item.id)
        assert free_contact.id in list_of_id


def check_free_contact(groups):
    free_contacts = []
    for i in range(0, len(groups)):
        group = groups[i]
        if db.get_contacts_not_in_group(group)[0] != []:
            free_contacts.append(db.get_contacts_not_in_group(group))
    return free_contacts