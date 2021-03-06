"""empty message

Revision ID: 89c0acef49e8
Revises: 
Create Date: 2021-12-12 11:01:10.135806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89c0acef49e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nidn', sa.String(length=30), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('alamat', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gambar',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('judul', sa.String(length=255), nullable=False),
    sa.Column('pathname', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('level', sa.BigInteger(), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('mahasiswa',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nim', sa.String(length=30), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('alamat', sa.String(length=255), nullable=False),
    sa.Column('dosen_satu', sa.BigInteger(), nullable=True),
    sa.Column('dosen_dua', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['dosen_dua'], ['dosen.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['dosen_satu'], ['dosen.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mahasiswa')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('gambar')
    op.drop_table('dosen')
    # ### end Alembic commands ###
