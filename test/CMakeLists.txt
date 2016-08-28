
project(MyHello)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package("Portaudio")

message("-->>> ${CMAKE_ARCH}")

if(PORTAUDIO_FOUND)
    IF(CMAKE_SYSTEM_NAME STREQUAL "Linux")
       SET(EXTRA_LIBS rt m asound pthread)
    ENDIF()

    add_executable(greet pa_devs.c)
    include_directories(${PORTAUDIO_INCLUDE_DIRS})
    target_link_libraries(greet ${PORTAUDIO_LIBRARY} ${EXTRA_LIBS})
else()
    message(FATAL_ERROR "Portaudio not found")
endif()