import todo_pb2_grpc
import todo_pb2
import grpc
import os
from flask import Flask
from google.protobuf.json_format import MessageToJson

host = os.getenv("HOST", "localhost")
app = Flask(__name__)

channel = grpc.insecure_channel(f"{host}:8080")
client = todo_pb2_grpc.TodoStub(channel)
# def run():
#     with grpc.insecure_channel(f"{host}:8080") as channel:
#         stub = todo_pb2_grpc.TodoStub(channel)
#         todo_request = todo_pb2.TodoItem(id = 1, text = "new todo")
#         reply = stub.createTodo(todo_request)
#         print("Response Received:")
#         print(reply)

#         todos_request = todo_pb2.TodoRequest()
#         reply = stub.readTodos(todos_request)
#         print("Response Received:")
#         print(reply)


# if __name__ == "__main__":
#     run()

@app.route("/createTodo")
def create_todo():
    todo_request = todo_pb2.TodoItem(id = 1, text = "new todo")
    response = client.createTodo(todo_request)
    print(response)
    return {"id": response.id, "text": response.text}

@app.route("/readTodos")
def read_todos():
    todo_request = todo_pb2.TodoRequest()
    response = client.readTodos(todo_request)
    print(response)
    return MessageToJson(response)
