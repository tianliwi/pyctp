# py_ctp
从 VNPY 分离出来的 Python  CTP 接口（用 pybind11 封装）

仅在 Linux 上运行

CTP 接口源码版本：6.6.1

pybind11 版本：2.6.2

参考：

https://github.com/vnpy/vnpy_ctp

https://github.com/shunfang/vnctp

---

## 使用方法

## 编译

在根目录下：

```
mkdir build
cd build
cmake ..
cmake --build . --config release
```

## 使用

生成的 .so 文件可以直接 import

```
from pyctpmd import MdApi
from pyctptd import TdApi

md = MdApi()
td = TdApi()

print("MdApi Version:" + md.GetApiVersion())
print("TdApi Version:" + td.GetApiVersion())
```

