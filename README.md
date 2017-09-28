
# conan-portaudio

[Conan](https://conan.io) package for [portaudio](http://www.portaudio.com/).

The packages generated with this **conanfile** can be found in [bintray](https://bintray.com/jgsogo/conan-packages/portaudio%3Ajgsogo).
In order to be able to compile the project you have to add it to your conan remotes:

```bash
$> conan remote add jgsogo-conan-packages https://api.bintray.com/conan/jgsogo/conan-packages
```

## Build status

 * `master` branch (package version) use last revision from the Portaudio repository.
 * `v19.20140130` branch (package version) use version v19.20140130 of Portaudio.
 * `v190600.20161030` branch (package version) use version v190600.20161030 of Portaudio.
 
 
<table>
    <thead>
        <tr>
            <th></th>
            <th colspan="3">Windows</th>
            <th colspan="4">Unix</th>
            <th>Macos</th>
        </tr>
    </thead>
    <tr>
        <td></td>
        <td>msvc 12</td>
        <td>msvc 14</td>
        <td>msvc 15</td>
        <td>gcc 4.9</td>
        <td>gcc 5.4</td>
        <td>gcc 6.3</td>
        <td>clang 4.0</td>
        <td>apple-clang 8.1</td>
    </tr>
    <tr>
        <td>master</td>
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/master/1" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/master/2" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/master/3" alt="Build status"/></a></td>        
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/master/1" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/master/2" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/master/3" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/master/4" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/master/5" alt="Build status"/></a></td>
    </tr>
    <tr>
        <td>v19.20140130</td>
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/v19.20140130/1" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/v19.20140130/2" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/v19.20140130/3" alt="Build status"/></a></td>        
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v19.20140130/1" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v19.20140130/2" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v19.20140130/3" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v19.20140130/4" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v19.20140130/5" alt="Build status"/></a></td>
    </tr>
    <tr>
        <td>v190600.20161030</td>
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/v190600.20161030/1" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/v190600.20161030/2" alt="Build status"/></a></td>        
        <td><a href="https://ci.appveyor.com/project/jgsogo/conan-portaudio"><img src="https://appveyor-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branch/v190600.20161030/3" alt="Build status"/></a></td>        
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v190600.20161030/1" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v190600.20161030/2" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v190600.20161030/3" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v190600.20161030/4" alt="Build status"/></a></td>
        <td><a href="https://travis-ci.org/jgsogo/conan-portaudio"><img src="https://travis-matrix-badges.herokuapp.com/repos/jgsogo/conan-portaudio/branches/v190600.20161030/5" alt="Build status"/></a></td>
    </tr>
</table>

