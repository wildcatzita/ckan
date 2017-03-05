# encoding: utf-8

import warnings

from sqlalchemy import exc as sa_exc
from sqlalchemy import *
from migrate import *
from migrate.changeset.constraint import UniqueConstraint


def upgrade(migrate_engine):
    # ignore reflection warnings
    print 'Hello from def upgrade'
    import pdb;pdb.set_trace();
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=sa_exc.SAWarning)
        metadata = MetaData()
        metadata.bind = migrate_engine
        group_table = Table('group', metadata, autoload=True)
        unique_id_name_constraint = UniqueConstraint(
            'id', 'name', table=group_table)
        unique_id_name_constraint.create()
