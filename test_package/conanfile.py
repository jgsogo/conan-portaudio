from conans import ConanFile, CMake
import os

class TestPortaudio(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        # equal to ./bin/portaudio_conan_test, but portable win: .\bin\portaudio_conan_test
        self.run(os.sep.join(["cd bin && .", "portaudio_conan_test"]))

    def imports(self):
        if self.settings.os == "Windows":
            self.copy(pattern="*.dll", dst="bin", src="bin")
            self.copy(pattern="*.pdb", dst="bin", src="bin")
	if self.settings.os == "Macos":
            self.copy(pattern="*.dylib", dst="bin", src="lib")
