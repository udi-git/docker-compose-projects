from flask import Flask , render_template, redirect, request
import docker

app = Flask(__name__)

client = docker.from_env()

@app.route('/')
def index():
    containers = client.containers.list(all=True)
    return render_template('index.html', containers=containers)

@app.route('/create', methods=['POST'])
def create_container():
    container_name = request.form.get('name')
    image_name = request.form.get('image')
    host_port = request.form.get('host_port')
    container_port = request.form.get('container_port')

    ports_dict = {f"{container_port}/tcp": host_port}
    

    client.containers.run(
        image=image_name,
        name=container_name,
        ports=ports_dict,
        detach=True
    ) 
            
    return redirect('/')

@app.route('/delete/<container_id>')
def delete_container(container_id):
    container = client.containers.get(container_id)
    container.stop()
    container.remove()

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

