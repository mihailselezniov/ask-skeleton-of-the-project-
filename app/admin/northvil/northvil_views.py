from app import *

admin.add_view(ModelView(Northvil_logs, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_variables, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_groups_vk, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_msg_page, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_users, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_sites, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_urls, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_msgs, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_photos_vk, db.session, category='Northvil'))
admin.add_view(ModelView(Northvil_counters_vk, db.session, category='Northvil'))