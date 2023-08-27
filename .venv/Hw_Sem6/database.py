import databases
import sqlalchemy
from sqlalchemy import ForeignKey
from settings import settings


database = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

products = sqlalchemy.Table("products", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("desc", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Integer)
    )

users = sqlalchemy.Table("users", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),
    sqlalchemy.Column("lastname", sqlalchemy.String(128)),
    sqlalchemy.Column("mail", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128))
    )

orders = sqlalchemy.Table("orders", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, ForeignKey("products.id"), nullable=False),
    )

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
metadata.create_all(engine)