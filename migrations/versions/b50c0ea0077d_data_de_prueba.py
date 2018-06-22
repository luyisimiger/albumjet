"""Data de prueba

Revision ID: b50c0ea0077d
Revises: a9bd6b41c2e0
Create Date: 2018-02-13 13:07:56.254000

"""
from alembic import op
from sqlalchemy.sql.expression import delete

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b50c0ea0077d'
down_revision = 'a9bd6b41c2e0'
branch_labels = None
depends_on = None


def upgrade():
    
    op.execute("""
        INSERT INTO users (nickname, email)
        VALUES ('user1', 'user1@gmail.com')
    """)

    op.execute("""
        INSERT INTO useralbum (iduser, idalbum, laminas)
        VALUES (1, 1, 250)
    """)

    op.execute("""
        INSERT INTO userlaminas (iduseralbum, idlamina, mark)
        SELECT useralbum.id, laminas.id, 0
        FROM albumjet
            INNER JOIN laminas ON laminas.idalbum = albumjet.id
            INNER JOIN useralbum ON useralbum.idalbum = albumjet.id
            INNER JOIN users ON users.id = useralbum.iduser
        WHERE albumjet.id = 1 AND users.id = 1
    """)





def downgrade():
    
    op.execute("""
        DELETE FROM users WHERE nickname = 'user1'
    """)

    op.execute("""
        DELETE FROM userlaminas
    """)

    op.execute("""
        DELETE FROM useralbum WHERE iduser = 1 AND idalbum = 1
    """)