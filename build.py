from conan.packager import ConanMultiPackager
import os, platform

if __name__ == "__main__":
    builder = ConanMultiPackager(username=username)
    builder.add_common_builds(shared_option_name="Portaudio:shared")
    filtered_builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        if settings["arch"] == "x86_64" and settings["build_type"] == "Release":
            filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds
    builder.run()
