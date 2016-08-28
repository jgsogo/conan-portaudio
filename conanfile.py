
import os
from conans import ConanFile
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
        command = None
        if os_info.is_linux:
            command = './configure && make'
        # TODO: Compile for windows
        self.run("cd %s && %s" % (self.FOLDER_NAME, command))

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join(self.FOLDER_NAME, "include"))
        # self.copy("*.lib", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib"))
        self.copy("*.a", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib", ".libs"))

    def package_info(self):
        self.cpp_info.libs = ["portaudio"]
