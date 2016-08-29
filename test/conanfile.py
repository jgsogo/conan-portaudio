
from conans import ConanFile, CMake
import os

# This easily allows to copy the package in other user or channel
channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "jgsogo")


class HelloReuseConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "portaudio/v19.20140130@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        # equal to ./bin/portaudio_conan_test, but portable win: .\bin\portaudio_conan_test
        self.run(os.sep.join([".","bin", "portaudio_conan_test"]))