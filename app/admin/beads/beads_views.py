from app import *

admin.add_view(ModelView(Beads_variables, db.session, category='Beads'))
admin.add_view(ModelView(Beads_groups_vk, db.session, category='Beads'))
admin.add_view(ModelView(Beads_reposts_vk, db.session, category='Beads'))
admin.add_view(ModelView(Beads_logs_vk, db.session, category='Beads'))
admin.add_view(ModelView(Beads_logs_general, db.session, category='Beads'))