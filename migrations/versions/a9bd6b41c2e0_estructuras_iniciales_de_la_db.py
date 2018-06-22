"""Estructuras iniciales de la db

Revision ID: a9bd6b41c2e0
Revises: 
Create Date: 2018-02-12 12:45:37.112000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9bd6b41c2e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    
    # ### commands auto generated by Alembic - please adjust! ###
    albumjet_table = op.create_table('albumjet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=256), nullable=False),
    sa.Column('descripcion', sa.String(length=256), nullable=False),
    sa.Column('laminas', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_nickname'), 'users', ['nickname'], unique=True)
    
    laminas_table = op.create_table('laminas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idalbum', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=256), nullable=False),
    sa.Column('descripcion', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['idalbum'], ['albumjet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('useralbum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iduser', sa.Integer(), nullable=False),
    sa.Column('idalbum', sa.Integer(), nullable=False),
    sa.Column('laminas', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idalbum'], ['albumjet.id'], ),
    sa.ForeignKeyConstraint(['iduser'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('iduser', 'idalbum')
    )
    op.create_table('userlaminas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iduseralbum', sa.Integer(), nullable=False),
    sa.Column('idlamina', sa.Integer(), nullable=False),
    sa.Column('mark', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['idlamina'], ['laminas.id'], ),
    sa.ForeignKeyConstraint(['iduseralbum'], ['useralbum.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('iduseralbum', 'idlamina')
    )
    # ### end Alembic commands ###


    op.bulk_insert(albumjet_table, [
        {"id": 1, "nombre": "Vive la Aventura Colombia",
        "descripcion": "Descripcion Vive la Aventura Colombia",
        "laminas": 250},
    ])
    
    laminas = 250
    lamina_rows = [
        
        {
            "idalbum": 1,
            "numero": i,
            "nombre": "Nombre Lamina # %d" % (i),
            "descripcion": "Descripcion Lamina # %d" % (i),
        }
        
        for i in range(1, laminas + 1)
    ]
    
    op.bulk_insert(laminas_table, lamina_rows)



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userlaminas')
    op.drop_table('useralbum')
    op.drop_table('laminas')
    op.drop_index(op.f('ix_users_nickname'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('albumjet')
    # ### end Alembic commands ###