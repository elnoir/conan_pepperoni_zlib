from conans import ConanFile, CMake, tools


class PepperonizlibConan(ConanFile):
    name = "pepperoni_zlib"
    version = "1.2.11"
    license = ""
    author = "Bittner Ede bittner.ede@gmail.com"
    url = ""
    description = ""
    topics = ("zlib", "minizip")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="zlib")
        git.clone("https://github.com/MrPepperoni/zlib.git", "master")

    def cmake_config(self):
        cmake = CMake(self)
        cmake.configure(source_folder="zlib")
        return cmake

    def build(self):
        cmake = self.cmake_config()
        cmake.build()

    def package(self):
        cmake = self.cmake_config()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.bindirs = ["bin"]

        if self.settings.os == "Windows":
            if self.settings.build_type != "Debug":
                self.cpp_info.libs = ["minizip.lib", "zlib.lib"]
            else:
                self.cpp_info.libs = ["minizipd.lib", "zlibd.lib"]
        else:
            self.cpp_info.libs = ["z", "minizip"]