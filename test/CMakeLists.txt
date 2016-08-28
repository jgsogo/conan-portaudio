
project(MyHello)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


IF(CMAKE_SYSTEM_NAME STREQUAL "Linux")
   SET(EXTRA_LIBS rt m asound pthread)
ENDIF()

add_executable(greet pa_devs.c)
include_directories(${CONAN_INCLUDE_DIRS})
target_link_libraries(greet ${CONAN_LIBS} ${EXTRA_LIBS})

macro(ADD_OSX_FRAMEWORK fwname target)
    find_library(FRAMEWORK_${fwname}
                NAMES ${fwname}
                PATHS ${CMAKE_OSX_SYSROOT}/System/Library
                PATH_SUFFIXES Frameworks
                NO_DEFAULT_PATH)
    if( ${FRAMEWORK_${fwname}} STREQUAL FRAMEWORK_${fwname}-NOTFOUND)
        message(ERROR ": Framework ${fwname} not found")
    else()
        target_link_libraries(${target} PUBLIC "${FRAMEWORK_${fwname}}/${fwname}")
        message(STATUS "Framework ${fwname} found at ${FRAMEWORK_${fwname}}")
    endif()
endmacro(ADD_OSX_FRAMEWORK)

if(APPLE)
   ADD_OSX_FRAMEWORK(CoreServices greet)
   ADD_OSX_FRAMEWORK(CoreFoundation greet)
   ADD_OSX_FRAMEWORK(AudioUnit greet)
   ADD_OSX_FRAMEWORK(AudioToolbox greet)
   ADD_OSX_FRAMEWORK(CoreAudio greet)
endif(APPLE)

