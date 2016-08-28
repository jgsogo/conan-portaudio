
import os
from conans import ConanFile, CMake
from conans.tools import os_info, SystemPackageTool


class PortaudioConan(ConanFile):
    name = "portaudio"
    version = "master"
    settings = "os", "compiler", "build_type", "arch"
    FOLDER_NAME = "portaudio_%s" % version.replace(".", "_")
    url="https://github.com/jgsogo/conan-portaudio"
    license=""  # TODO: Check licence
    exports = ["FindPortaudio.cmake",]

    def system_requirements(self):
        pack_name = None
        if os_info.is_linux:
            pack_name = "libasound2-dev"

        if pack_name:
            installer = SystemPackageTool()
            installer.update()  # Update the package database
            installer.install(pack_name)  # Install the package

    def source(self):
        self.run("git clone https://git.assembla.com/portaudio.git {}".format(self.FOLDER_NAME))

    def build(self):
        if self.settings.os == "Linux" or self.settings.os == "Macos":
            command = './configure && make'
            self.run("cd %s && %s" % (self.FOLDER_NAME, command))
        else:
            build_dirname = "_build"
            cmake = CMake(self.settings)
            if self.settings.os == "Windows":
                self.run("IF not exist {} mkdir {}".format(build_dirname, build_dirname))
            else:
                self.run("mkdir {}".format(build_dirname))

            cmake_command = 'cd {} && cmake {} {}'.format(build_dirname, os.path.join("..", self.FOLDER_NAME), cmake.command_line)
            self.output.info(cmake_command)
            self.run(cmake_command)

            build_command = "cd {} && cmake --build . {}".format(build_dirname, cmake.build_config)
            self.output.info(build_command)
            self.run(build_command)

    def package(self):
        self.copy("FindPortaudio.cmake", ".", ".")
        self.copy("*.h", dst="include", src=os.path.join(self.FOLDER_NAME, "include"))
        self.copy("*.lib", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib"))
        self.copy("*.a", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib", ".libs"))

    def package_info(self):
        if self.settings.os == "Linux" or self.settings.os == "Macos":
            self.cpp_info.libs = ["portaudio"]
        else:
            if self.settings.arch == "x86":
                self.cpp_info.libs = ["portaudio_x86"]
            else:
                self.cpp_info.libs = ["portaudio_x64"]

