from model.group import Group
import random

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = map(app.group.clean_group, db.get_group_list())
    old_groups_l = list(old_groups)
    group = random.choice(old_groups_l)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups_l) - 1 == app.group.count()
    new_groups = map(app.group.clean_group, db.get_group_list())
    #удаление элементов списка с индексом 0
    old_groups_l.remove(group)
    assert old_groups_l == list(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)