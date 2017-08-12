
from conans import ConanFile, CMake
import os

class TestPortaudio(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        # equal to ./bin/portaudio_conan_test, but portable win: .\bin\portaudio_conan_test
        self.run(os.sep.join([".","bin", "portaudio_conan_test"]))
