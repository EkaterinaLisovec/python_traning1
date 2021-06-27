# -*- coding: utf-8 -*-
from model.group import Group
#если хотим загружать данные из data.groups.py, то указать переменную на вход: data_groups
#это описано в conftest
import allure



def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = map(app.group.clean_group, db.get_group_list())
    with allure.step('When I add a group %s to the list' %group):
        app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = map(app.group.clean_group, db.get_group_list())
        list(new_groups)
        #добавление новой группы в список
        list(old_groups).append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)