
project(MyHello)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package("Portaudio")

IF(PORTAUDIO_FOUND)
    add_executable(greet pa_devs.c)
    include_directories(${PORTAUDIO_INCLUDE_DIRS})
    target_link_libraries(greet PUBLIC ${PORTAUDIO_LIBRARIES})
ELSE()
    message(FATAL_ERROR "Portaudio not found")
ENDIF()
