
echo "生成rpc代码"

python -m grpc_tools.protoc --python_out=../proto --grpc_python_out=../proto -I. agent.proto

echo "生成完毕"
