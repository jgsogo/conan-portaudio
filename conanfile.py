import os, subprocess
from conans import ConanFile, CMake
from conans.tools import os_info, SystemPackageTool, download, untargz, replace_in_file

class PortaudioConan(ConanFile):
    name = "portaudio"
    version = "rc.v190600.20161001"
    settings = "os", "compiler", "build_type", "arch"
    FOLDER_NAME = "portaudio"
    url = "https://github.com/jgsogo/conan-portaudio"
    license = "http://www.portaudio.com/license.html"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports = ["FindPortaudio.cmake",]

    WIN = {'build_dirname': "_build"}

    def rpm_package_installed(self, package):
        p = subprocess.Popen(['rpm', '-q', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = p.communicate()
        return 'install ok' in out or 'not installed' not in out

    def ensure_rpm_dependency(self, package):
        if not self.rpm_package_installed(package):
            self.output.warn(package + " is not installed in this machine! Conan will try to install it.")
            # Note: yum is automatically redirected to dnf on modern Fedora distros (see 'man yum2dnf')
            self.run("sudo yum install -y " + package)
            if not self.rpm_package_installed(package):
                self.output.error(package + " Installation doesn't work... install it manually and try again")
                exit(1)

    def system_requirements(self):
        pack_name = None
        if os_info.is_linux:
            if os_info.with_apt:
                pack_name = "libasound2-dev"
            elif os_info.with_yum:
                self.ensure_rpm_dependency("alsa-lib-devel")

        if pack_name:
            installer = SystemPackageTool()
            installer.update()  # Update the package database
            installer.install(pack_name)  # Install the package

    def source(self):
        zip_name = 'pa_rc_v190600_20161001.tgz'
        url = 'http://www.portaudio.com/archives/pa_rc_v190600_20161001.tgz'
        download(url, zip_name)
        untargz(zip_name)  # Creates a portaudio directory
        os.unlink(zip_name)
        if self.settings.os != "Windows":
            self.run("chmod +x ./%s/configure" % self.FOLDER_NAME)

    def build(self):
        if self.settings.os == "Linux" or self.settings.os == "Macos":
            command = './configure && make'
            self.run("cd %s && %s" % (self.FOLDER_NAME, command))
        else:
            # We must disable ksguid.lib: https://app.assembla.com/spaces/portaudio/tickets/228-ksguid-lib-linker-issues/details
            replace_in_file(os.path.join(self.FOLDER_NAME, "CMakeLists.txt"), "ADD_DEFINITIONS(-D_CRT_SECURE_NO_WARNINGS)", "ADD_DEFINITIONS(-D_CRT_SECURE_NO_WARNINGS -DPAWIN_WDMKS_NO_KSGUID_LIB)")

            build_dirname = self.WIN['build_dirname']
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
        if self.settings.os == "Windows":
            build_dirname = self.WIN['build_dirname']
            self.copy("*.lib", dst="lib", src=os.path.join(build_dirname, str(self.settings.build_type)))
            if self.options.shared:
                self.copy("*.dll", dst="bin", src=os.path.join(build_dirname, str(self.settings.build_type)))
        else:
            if self.options.shared:
                if self.settings.os == "Macos":
                    self.copy(pattern="*.dylib", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib", ".libs"))
                else:
                    self.copy(pattern="*.so*", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib", ".libs"))
            else:
                self.copy("*.a", dst="lib", src=os.path.join(self.FOLDER_NAME, "lib", ".libs"))

    def package_info(self):
        base_name = "portaudio"
        if self.settings.os == "Windows":
            if not self.options.shared:
                base_name += "_static"
            base_name += "_x86" if self.settings.arch == "x86" else "_x64"
        self.cpp_info.libs = [base_name]

