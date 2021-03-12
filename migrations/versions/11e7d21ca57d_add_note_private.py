"""add Note.private

Revision ID: 11e7d21ca57d
Revises: 7747b61d91fc
Create Date: 2021-03-11 09:32:10.876681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11e7d21ca57d'
down_revision = '7747b61d91fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note_model', sa.Column('private', sa.Boolean(), server_default='true', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # https: // alembic.sqlalchemy.org / en / latest / batch.html
    with op.batch_alter_table("note_model") as batch_op:
        batch_op.drop_column('private')
    # ### end Alembic commands ###