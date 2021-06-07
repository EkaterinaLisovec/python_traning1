# -*- coding: utf-8 -*-
from model.group import Group
#если хотим загружать данные из data.groups.py, то указать переменную на вход: data_groups
#это описано в conftest


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    #добавление новой группы в список
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)