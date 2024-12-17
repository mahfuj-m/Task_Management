import argparse
import signal
from flask import Flask, request, jsonify
from validation import sanitize_input, check_empty
from data import StorageHandler as SH

parser = argparse.ArgumentParser()
parser.add_argument('--file', help="JSON file that stores the data")
parser.add_argument('--save', help="If you want to save the updates to the file")
args = parser.parse_args()

app = Flask(__name__) #app creation
tasks=[]

@app.route('/tasks/', methods =['GET'])
def getTasks():
    return jsonify(tasks)

@app.route('/addtask/', methods=['POST'])
def createTask():    
    name = request.form['name']
    if check_empty(name):
        return jsonify('Task must followed by a Title')
    id = tasks[-1]['id']+1 if (len(tasks) > 0) else 0
    new_tasks = {
        'id' : id,
        'name' : name,
        'desc' : sanitize_input(request.form['desc'])
    }
    tasks.append(new_tasks)
    return jsonify(new_tasks)



@app.route('/task/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def singelTask(id):
    if request.method == 'GET':
        check = 0
        for task in tasks:
            if task['id'] == id:
                check = 1
                return jsonify(task)
        if check == 0:
            return jsonify('No tasks available')
    if request.method == 'PUT':
        for task in tasks:
            if task['id'] == id:
                name = request.form['name']
                if check_empty(name):
                    return jsonify('Task must followed by a Title')
                updated_task = {
                                'id' : id,
                                'name' : name,
                                'desc' : sanitize_input(request.form['desc'])
                                }
                task.update(updated_task)
                return jsonify(updated_task)

    if request.method == 'DELETE':
        check = 0
        for index, task in enumerate(tasks):
            if task['id'] == id:
                check = 1
                tasks.pop(index)
                return jsonify(tasks)
        if check == 0:
            return jsonify('Task doesn\' exists')

# Signal handler to trigger on shutdown
def handle_shutdown_signal(signum, frame):
    if args.save:

        data_saver.save(tasks)
    print("Server shutted down")
    exit(0)

signal.signal(signal.SIGTERM, handle_shutdown_signal)  # Handle termination
signal.signal(signal.SIGINT, handle_shutdown_signal)  # Handle interrupt (Ctrl+C)

if __name__=='__main__':
    try:
        if args.file:
            data_saver = SH(args.file)
            data = data_saver.load() 
            if  not check_empty(data):
                for item in data:
                    tasks.append(item)

        app.run(debug=True, use_reloader=False)
    except Exception as e:
        pass



