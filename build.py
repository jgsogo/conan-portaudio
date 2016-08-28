from conan.packager import ConanMultiPackager
import os


username = os.getenv("CONAN_USERNAME", "jgsogo")


if __name__ == "__main__":
    builder = ConanMultiPackager(username=username)
    builder.add_common_builds(shared_option_name="Portaudio:shared")
    filtered_builds = []
    for settings, options in builder.builds:
        if settings["arch"] == "x86_64":
             filtered_builds.append([settings, options])
    builder.builds = filtered_builds
    builder.run()
