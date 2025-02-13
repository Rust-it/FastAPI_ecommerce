from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from datetime import date

from app.backend.db import Base


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    rating_id = Column(Integer, ForeignKey('ratings.id'), nullable=True)
    comment = Column(String, nullable=True)
    comment_date = Column(Date, default=date.today())
    is_active = Column(Boolean, default=True)

    rating = relationship('Rating', back_populates='review')