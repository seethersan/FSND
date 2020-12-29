"""empty message

Revision ID: 84ee5a2cef47
Revises: a6f9d2b0b058
Create Date: 2020-12-28 10:28:47.786793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84ee5a2cef47'
down_revision = 'a6f9d2b0b058'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
