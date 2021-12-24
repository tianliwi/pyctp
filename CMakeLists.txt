CMAKE_MINIMUM_REQUIRED(VERSION 3.4)
# 指定为C++11版本
SET(CMAKE_CXX_STANDARD 11)

PROJECT(PYCTP)

# 添加源文件列表
FILE(GLOB MD_SRC_LIST "${PROJECT_SOURCE_DIR}/src/pyctpmd.cpp")
FILE(GLOB TD_SRC_LIST "${PROJECT_SOURCE_DIR}/src/pyctptd.cpp")

# 指定头文件位置
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/include)

# 附加python头文件(macOS)
# INCLUDE_DIRECTORIES(/Users/gavin/.pyenv/versions/3.8.5/include/python3.8)

# 附加python头文件
INCLUDE_DIRECTORIES(/usr/include/python3.8)

# 指定 ctp 动态库位置
# 添加共享库搜索路径
LINK_DIRECTORIES(${PROJECT_SOURCE_DIR}/libs)

# 指定输出动态库的目录位置
SET(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/target)

####### md

# 指定生成动态库pyctpmd
ADD_LIBRARY(pyctpmd SHARED ${MD_SRC_LIST})

# 指定输出动态库扩展名
SET_TARGET_PROPERTIES(pyctpmd PROPERTIES SUFFIX ".so" PREFIX "")

# 指定链接库(ctp so 动态库仅在 Linux 有效)
TARGET_LINK_LIBRARIES(pyctpmd thostmduserapi_se)

######## trader

# 指定生成动态库pyctptd
ADD_LIBRARY(pyctptd SHARED ${TD_SRC_LIST})

# 指定输出动态库扩展名
SET_TARGET_PROPERTIES(pyctptd PROPERTIES SUFFIX ".so" PREFIX "")

# 指定链接库(ctp so 动态库仅在 Linux 有效)
TARGET_LINK_LIBRARIES(pyctptd thosttraderapi_se)
