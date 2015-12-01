from app import *

admin.add_view(ModelView(Lumiera_variables, db.session, category='Lumiera'))
admin.add_view(ModelView(Lumiera_sprashivai_qa, db.session, category='Lumiera'))
admin.add_view(ModelView(Lumiera_wall, db.session, category='Lumiera'))