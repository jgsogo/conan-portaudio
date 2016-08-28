
project(MyHello)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

IF(CMAKE_SYSTEM_NAME STREQUAL "Linux")
   SET(EXTRA_LIBS rt m asound pthread)
ENDIF()

add_executable(greet pa_devs.c)
target_link_libraries(greet ${CONAN_LIBS} ${EXTRA_LIBS})