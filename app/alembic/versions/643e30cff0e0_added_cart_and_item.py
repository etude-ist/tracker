# flake8: noqa
"""added cart and item

Revision ID: 643e30cff0e0
Revises: 
Create Date: 2019-04-15 20:12:54.185192

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '643e30cff0e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('cart_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('external_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('value', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    op.drop_table('cart')
    # ### end Alembic commands ###
