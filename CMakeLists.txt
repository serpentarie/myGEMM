cmake_minimum_required(VERSION 3.10)
project(myGEMM)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -Wall")

set(SRCDIR src)
set(BINDIR bin)
set(OBJDIR obj)
set(SCRDIR scripts)

find_package(OpenCL REQUIRED)
find_package(clBLAS CONFIG REQUIRED)

set(CPPSOURCES ${SRCDIR}/main.cpp ${SRCDIR}/clGEMM.cpp ${SRCDIR}/libclblas.cpp)

add_executable(${PROJECT_NAME} ${CPPSOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE ${SRCDIR})

target_link_libraries(${PROJECT_NAME} PRIVATE OpenCL::OpenCL clBLAS)
target_compile_definitions(${PROJECT_NAME} PRIVATE CL_TARGET_OPENCL_VERSION=100)

set(EXECUTABLE_OUTPUT_PATH ${BINDIR})
