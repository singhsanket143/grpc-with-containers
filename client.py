import todo_pb2_grpc
import todo_pb2
import grpc
import os

host = os.getenv("HOST", "localhost")

def run():
    with grpc.insecure_channel(f"{host}:8080") as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        todo_request = todo_pb2.TodoItem(id = 1, text = "new todo")
        reply = stub.createTodo(todo_request)
        print("Response Received:")
        print(reply)

        todos_request = todo_pb2.TodoRequest()
        reply = stub.readTodos(todos_request)
        print("Response Received:")
        print(reply)


if __name__ == "__main__":
    run()