# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/bokaichen/user/nlohman_json

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/bokaichen/user/nlohman_json/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/nlohman_json.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/nlohman_json.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/nlohman_json.dir/flags.make

CMakeFiles/nlohman_json.dir/main.cpp.o: CMakeFiles/nlohman_json.dir/flags.make
CMakeFiles/nlohman_json.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/bokaichen/user/nlohman_json/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/nlohman_json.dir/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/nlohman_json.dir/main.cpp.o -c /Users/bokaichen/user/nlohman_json/main.cpp

CMakeFiles/nlohman_json.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/nlohman_json.dir/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/bokaichen/user/nlohman_json/main.cpp > CMakeFiles/nlohman_json.dir/main.cpp.i

CMakeFiles/nlohman_json.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/nlohman_json.dir/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/bokaichen/user/nlohman_json/main.cpp -o CMakeFiles/nlohman_json.dir/main.cpp.s

# Object files for target nlohman_json
nlohman_json_OBJECTS = \
"CMakeFiles/nlohman_json.dir/main.cpp.o"

# External object files for target nlohman_json
nlohman_json_EXTERNAL_OBJECTS =

nlohman_json: CMakeFiles/nlohman_json.dir/main.cpp.o
nlohman_json: CMakeFiles/nlohman_json.dir/build.make
nlohman_json: CMakeFiles/nlohman_json.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/bokaichen/user/nlohman_json/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable nlohman_json"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/nlohman_json.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/nlohman_json.dir/build: nlohman_json

.PHONY : CMakeFiles/nlohman_json.dir/build

CMakeFiles/nlohman_json.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/nlohman_json.dir/cmake_clean.cmake
.PHONY : CMakeFiles/nlohman_json.dir/clean

CMakeFiles/nlohman_json.dir/depend:
	cd /Users/bokaichen/user/nlohman_json/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/bokaichen/user/nlohman_json /Users/bokaichen/user/nlohman_json /Users/bokaichen/user/nlohman_json/cmake-build-debug /Users/bokaichen/user/nlohman_json/cmake-build-debug /Users/bokaichen/user/nlohman_json/cmake-build-debug/CMakeFiles/nlohman_json.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/nlohman_json.dir/depend
