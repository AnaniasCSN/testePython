from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Armazenamento temporário em memória (Lista Python)
# Em uma aplicação de produção, este ponto seria conectado a um Banco de Dados (ex: SQLite ou MySQL)
tasks_db = []

# Rota Principal: Renderiza a Interface HTML
@app.route('/')
def index():
    return render_template('index.html')

# API Rota GET: Retorna todas as tarefas registradas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks_db)

# API Rota POST: Adiciona uma nova tarefa
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    
    if not data or 'task' not in data:
        return jsonify({'error': 'Dados inválidos'}), 400
    
    new_task = data['task'].strip()
    if new_task:
        tasks_db.append(new_task)
        return jsonify({'message': 'Tarefa criada com sucesso'}), 201
    
    return jsonify({'error': 'A tarefa não pode estar vazia'}), 400

# API Rota DELETE: Remove uma tarefa pelo índice
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks_db):
        removed = tasks_db.pop(task_id)
        return jsonify({'message': f'Tarefa "{removed}" removida com sucesso'}), 200
    
    return jsonify({'error': 'Tarefa não encontrada'}), 404

# Execução do servidor em modo de desenvolvimento
#if __name__ == '__main__':
 #   app.run(debug=True, port=5000)
    import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)