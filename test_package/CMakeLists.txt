project(PortaudioConanTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(portaudio_conan_test main.c)
target_link_libraries(portaudio_conan_test PUBLIC ${CONAN_LIBS})
set_target_properties(portaudio_conan_test PROPERTIES LINK_FLAGS "${CONAN_EXE_LINKER_FLAGS}")

