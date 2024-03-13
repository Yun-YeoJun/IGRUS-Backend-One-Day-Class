from flask import Flask, render_template, request, redirect, flash
from database import Database
import time


app = Flask(__name__)


@app.route('/')
def home():
    db = Database()
    rows = db.execute_sql('select * from task;')
    return render_template('home.html', all_task_list=rows)


@app.route('/task/create', methods=['post'])
def create_task():
    content = request.get_json()['content']
    db = Database()
    db.execute_sql(f'''
        insert into task (content, created_at) values ('{content}', '{time.strftime('%Y-%m-%d %H:%M:%S')}')
    ''')
    return {"message": "done"}


@app.route('/task/update/status/<task_id>')
def check_task(task_id):
    print(task_id)
    db = Database()
    db.execute_sql(f'''
        update task set status=if(task.status=1,0,1) where id={task_id};
    ''')
    db.execute_sql(f'''
        update task set updated_at='{time.strftime('%Y-%m-%d %H:%M:%S')}' where id={task_id};
    ''')
    return {"message": "Done"}


@app.route('/task/update/content/<task_id>', methods=['post'])
def update_task(task_id):
    new_content = request.get_json()['new_content']
    db = Database()
    db.execute_sql(f'''
        update task set content='{new_content}' where id={task_id};
    ''')
    db.execute_sql(f'''
        update task set updated_at='{time.strftime('%Y-%m-%d %H:%M:%S')}' where id={task_id};
    ''')
    return {"message": "Done"}


@app.route('/task/delete/<task_id>')
def delete_task(task_id):
    db = Database()
    db.execute_sql(f'''delete from task where id={task_id}''')
    return {"message": "Done"}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
