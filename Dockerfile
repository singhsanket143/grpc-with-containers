FROM python
RUN mkdir /service
COPY todo.proto /service/todo.proto
COPY server.py /service/server.py
COPY requirements.txt /service/requirements.txt
WORKDIR /service
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. todo.proto

EXPOSE 8080
ENTRYPOINT [ "python3", "server.py" ]