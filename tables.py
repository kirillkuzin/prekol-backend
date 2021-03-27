import sqlalchemy as sa

# from config import DATABASE_URL


metadata = sa.MetaData()
# engine = sa.create_engine(DATABASE_URL)


cities = sa.Table(
    'cities',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String),
    sa.Column('image_url', sa.String)
)

places = sa.Table(
    'places',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String),
    sa.Column('type', sa.String),
    sa.Column('description', sa.String),
    sa.Column('lon', sa.Float),
    sa.Column('lat', sa.Float),
    sa.Column('image_url', sa.String),
    sa.Column('city_id', sa.Integer, sa.ForeignKey('cities.id'))
)

user_places = sa.Table(
    'user_places',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String),
    sa.Column('place_id', sa.Integer, sa.ForeignKey('places.id'))
)

# metadata.create_all(engine)
