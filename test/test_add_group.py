# -*- coding: utf-8 -*-
from model.group import Group
#если хотим загружать данные из data.groups.py, то указать переменную на вход: data_groups
#это описано в conftest


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = map(app.group.clean_group, db.get_group_list())
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    new_groups = map(app.group.clean_group, db.get_group_list())
    list(new_groups)
    #добавление новой группы в список
    list(old_groups).append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)