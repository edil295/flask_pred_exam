"""empty message

Revision ID: 69c46de5dff1
Revises: 
Create Date: 2022-07-19 14:14:41.893074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69c46de5dff1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=44), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.String(length=32), nullable=True),
    sa.Column('item', sa.String(length=64), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('date_in', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    op.drop_table('user')
    # ### end Alembic commands ###
