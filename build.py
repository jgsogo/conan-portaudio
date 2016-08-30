from conan.packager import ConanMultiPackager
import os


username = os.getenv("CONAN_USERNAME", "jgsogo")


class UploadRecipeOnly(ConanMultiPackager):
    def run(self):
        self._pack()
        self._upload_packages(upload_all=False)


if __name__ == "__main__":
    builder = UploadRecipeOnly(username=username)
    builder.add_common_builds(shared_option_name="Portaudio:shared")
    filtered_builds = []
    for settings, options in builder.builds:
        if settings["arch"] == "x86_64":
             filtered_builds.append([settings, options])
    builder.builds = filtered_builds
    builder.run()
