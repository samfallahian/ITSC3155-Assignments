from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create_order(db: Session, order):
    db_order = models.Order(
        customer_name=order.customer_name,
        description=order.description
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_orders(db: Session):
    return db.query(models.Order).all()


def get_one_orders(db: Session, order_id):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def update(db: Session, order_id, order):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    update_data = order.dict(exclude_unset=True)
    db_order.update(update_data, synchronize_session=False)
    db.commit()
    return db_order.first()


def delete(db: Session, order_id):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    db_order.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
