
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

    def system_requirements(self):
        pack_name = None
        if os_info.is_linux:
            pack_name = "libasound-dev"

        if pack_name:
            installer = SystemPackageTool()
            installer.update()  # Update the package database
            installer.install(pack_name)  # Install the package

    def source(self):
        self.run("git clone https://git.assembla.com/portaudio.git {}".format(self.FOLDER_NAME))

    def build(self):
        if self.settings.os == "Linux" or self.settings.os == "Macos":
            configure_args = ""
            if self.settings.arch == 'x86':
                configure_args = 'CC="gcc -m32" CXX="g++ -m32"'
            else:
                configure_args = 'CC="gcc -m64" CXX="g++ -m64"'
            command = './configure {} && make'.format(configure_args)
            self.run("cd %s && %s" % (self.FOLDER_NAME, command))
        else:
            build_dirname = "_build"
            cmake = CMake(self.settings)
            if self.settings.os == "Windows":
                self.run("IF not exist {} mkdir {}".format(build_dirname, build_dirname))
            else:
                self.run("mkdir {}".format(build_dirname))
            self.output.warn('cd {} && cmake {} {}'.format(build_dirname, os.path.join("..", self.FOLDER_NAME), cmake.command_line))
            self.run('cd {} && cmake {} {}'.format(build_dirname, os.path.join("..", self.FOLDER_NAME), cmake.command_line))
            self.output.warn("cd {} && cmake --build . {}".format(build_dirname, cmake.build_config))
            self.run("cd {} && cmake --build . {}".format(build_dirname, cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join(self.FOLDER_NAME, "include"))
        self.copy("*.lib", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib"))
        self.copy("*.a", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib", ".libs"))

    def package_info(self):
        self.cpp_info.libs = ["portaudio"]
