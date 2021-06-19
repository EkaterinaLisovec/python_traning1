from model.group import Group
from random import randrange
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = map(app.group.clean_group, db.get_group_list())
    old_groups_l = list(old_groups)
    group_old = random.choice(old_groups_l)
    index = old_groups_l.index(group_old)
    #index = randrange(len(old_groups_l))
    group = Group(name="New group")
    group.id = group_old.id
    app.group.modify_group_by_id(group_old.id, group)
    assert len(old_groups_l) == app.group.count()
    new_groups = map(app.group.clean_group, db.get_group_list())
    old_groups_l[index] = group
    assert sorted(old_groups_l, key=Group.id_or_max) == sorted(list(new_groups), key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)