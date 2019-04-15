import sqlalchemy as sq

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.base import Base


class Cart(Base):

    __tablename__ = 'cart'

    id = sq.Column(UUID(as_uuid=True), primary_key=True)

    items = relationship("Item", back_populates="cart")


class Item(Base):

    __tablename__ = 'item'

    id = sq.Column(UUID(as_uuid=True), primary_key=True)
    cart_id = sq.Column(UUID(as_uuid=True), sq.ForeignKey('cart.id'))
    external_id = sq.Column(sq.String)
    name = sq.Column(sq.String, nullable=True)
    value = sq.Column(sq.Numeric, nullable=True)

    cart = relationship("Cart", back_populates="items")
