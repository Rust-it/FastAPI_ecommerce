from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from sqlalchemy import insert, select
from app.routers.auth import get_current_user
from statistics import mean

from app.backend.db_depends import get_db
from app.schemas import CreateReview
from app.models.reviews import Review
from app.models.rating import Rating
from app.models.user import User
from app.models.products import Product

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.get('/')
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)],):
    reviews = await db.scalars(select(Review).where(Review.is_active == True))
    return reviews.all()


@router.get('/{product_id}')
async def products_reviews(db: Annotated[AsyncSession, Depends(get_db)], product_id: int):
    products_reviews = await db.scalar(select(Review).where(
        Review.product_id == product_id,
        Review.is_active == True))
    if products_reviews is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Review not found'
        )
    return products_reviews


@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_review(db: Annotated[AsyncSession, Depends(get_db)], create_review: CreateReview, get_user: Annotated[dict, Depends(get_current_user)]):
    if get_user.get('is_customer'):
        requested_product = await db.scalar(select(Product).where(Product.id == create_review.product_id))
        result = await db.execute(insert(Rating).values(
            grade=create_review.grade,
            user_id=get_user.get('id'),
            product_id=create_review.product_id
        ))
        inserted_rate_id = result.inserted_primary_key[0]
        product_review = await db.execute(insert(Review).values(
            user_id=get_user.get('id'),
            product_id=create_review.product_id,
            rating_id=inserted_rate_id,
            comment=create_review.comment
        ))
        all_evaluates = await db.scalars(select(Rating.grade).where(
            Rating.product_id == create_review.product_id))
        all_evaluates = all_evaluates.all()
        product_rate = mean(all_evaluates)
        requested_product.rating = product_rate
        await db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }
    else:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to use this method")


@router.delete('/')
async def delete_reviews(db: Annotated[AsyncSession, Depends(get_db)], review_id: int, get_user: Annotated[dict, Depends(get_current_user)]):
    if get_user.get('is_admin'):
        review = await db.scalar(select(Review).where(Review.id == review_id))
        if review is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no review found'
            )
        rating = await db.scalar(select(Rating).where(Rating.id == review.rating_id))
        if rating is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no rating found'
            )
        review.is_active = False
        rating.is_active = False

        requested_product = await db.scalar(select(Product).where(
            Product.id == review.product_id))
        all_evaluates = await db.scalars(
            select(Rating.grade).where(
                Rating.product_id == requested_product.id,
                Rating.is_active == True))
        all_evaluates = all_evaluates.all()
        product_rate = mean(all_evaluates)
        requested_product.rating = product_rate
        await db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Review delete is successful'
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="You are not authorized to use this method")