from __init__ import app
from views import user as user_view
from models import user


from __init__ import engine, Base

#Create tables
Base.metadata.create_all(bind=engine)

#Include routers
app.include_router(user_view.router)
