from concurrent import futures
import grpc
import todo_pb2
import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServicer):

    def __init__(self):
        self.todos = []

    def createTodo(self, request, context):
        print("Executing the create todo rpc")
        print(request)
        reply = todo_pb2.TodoItem()
        reply.id = request.id
        reply.text = request.text + "added from server"
        self.todos.append(reply)
        return reply
    
    def readTodos(self, request, context):
        print("Executing the read todos rpc")
        print(request)
        reply = todo_pb2.TodoItems()
        reply.items.append(self.todos[0])
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
    server.add_insecure_port("[::]:8080")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":  
    serve()
    print("by")