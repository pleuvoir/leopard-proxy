


## 引入数据组件

https://github.com/bmoscon/cryptofeed

网络连接不通，作者回复
https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate

可以DEBUG进去查看调用路径


## await

```python
async def do_them():
    for event, callback, multi in self._subscribers:
    await self._initialize(event, callback, multi)
```

这种await必须在异步函数中执行，即async的def方法

await 会让出当前线程，类似于yield 而不是在这里阻塞等待，这里需要着重理解，不是异步转同步的意思。在协程中遇到耗时操作就使用 await

https://www.cnblogs.com/yanzi-meng/p/8533734.html



## 引入grpc

https://www.cnblogs.com/guyouyin123/p/16133065.html

生成的文件需要改动导入包的路径
import agent_pb2 as agent__pb2
from rpc.proto import agent_pb2 as agent__pb2

from 从哪个包 import 文件名称


## 形参可以直接传入一个字典，这样会根据形参的名称自动填值

```python
# 初始化日志
logger.initLogger(**config.log)
# 启动grpc
grpc.start_grpc(**config.grpc)
```

记得要带上**


## 协程使用


