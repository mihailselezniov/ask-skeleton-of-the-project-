# -*- coding: utf-8 -*-
from app import *
from datatables import ColumnDT, DataTables

@app.route('/')
@app.route('/index')
def index():
    new_reposts = Beads_reposts_vk.query.filter_by(post=False)\
        .filter(Beads_reposts_vk.group_id==Beads_groups_vk.id)\
        .filter(Beads_groups_vk.boolean==True)\
        .order_by(Beads_reposts_vk.created_at).all()
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    return render_template("index.html", title='Home', user=user, new_reposts=new_reposts)

@app.route('/look/')
def look():
    return "<h1>Ask</h1>"

def _default_value_view(chain):
    if chain == 'None':
        return None
    return chain

def _timestamp_value_view(chain):
    try:
        hour = 60*60
        dif = 3*hour # UTC+3
        day = 24*hour
        st = datetime.datetime.fromtimestamp(int(chain)+dif).strftime('%d-%m-%Y %H:%M:%S')
        return str(st)
    except:
        return chain

@app.route('/lumiera_qa_json')
def lumiera_qa_json():
    columns = list()
    columns.append(ColumnDT('question', filter=_default_value_view))
    columns.append(ColumnDT('answer', filter=_default_value_view))
    columns.append(ColumnDT('timestamp', filter=_timestamp_value_view))
    return jsonify(**DataTables(request, Lumiera_sprashivai_qa, db.session.query(Lumiera_sprashivai_qa), columns).output_result())