# This file is part of s-dftd3.
# SPDX-Identifier: LGPL-3.0-or-later
#
# s-dftd3 is free software: you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# s-dftd3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with s-dftd3.  If not, see <https://www.gnu.org/licenses/>.
"""
FFI builder module for s-dftd3 for usage from meson or standalone execution.

Since meson has the full knowledge about the build, it will handle
the generation of the C definitions in the meson.build file rather
than in the FFI builder. This allows it to correctly keep track of
dependencies and updates in the build process.

When executed directly, the FFI builder:
- Uses the C compiler to preprocess the header file of s-dftd3
  because the CFFI C parser cannot handle certain C preprocessor constructs.
- Automatically resolves dependencies using pkg-config (if available),
  or falls back to standard include and library paths if the package
  is installed in a custom location.
"""
import os
import cffi

library = "s-dftd3"
include_header = '#include "dftd3.h"'
prefix_var = "SDFTD3_PREFIX"
if prefix_var not in os.environ:
    prefix_var = "CONDA_PREFIX"

# Adjust include path based on the project structure
current_dir = os.path.dirname(os.path.abspath(__file__))
subtree_include_path = os.path.join(current_dir, "subprojects", "s-dftd3", "include")
if os.path.exists(os.path.join(subtree_include_path, "dftd3.h")):
    include_dirs = [subtree_include_path]
else:
    include_dirs = []  # Leave it empty if no alternative path is found

kwargs = dict(libraries=[library], include_dirs=include_dirs)
cflags = [f"-I{path}" for path in include_dirs]

cc = os.environ["CC"] if "CC" in os.environ else "cc"

if __name__ == "__main__":
    import sys

    header_file = sys.argv[1]
    module_name = sys.argv[2]

    with open(header_file) as f:
        cdefs = f.read()
else:
    import subprocess

    try:
        import pkgconfig

        if not pkgconfig.exists(library):
            raise ModuleNotFoundError("Unable to find pkg-config package 's-dftd3'")
        if pkgconfig.installed(library, "< 0.4"):
            raise Exception(
                "Installed 's-dftd3' version is too old, 0.4 or newer is required"
            )

        kwargs.update(pkgconfig.parse(library))
        cflags.extend(pkgconfig.cflags(library).split())

    except ModuleNotFoundError:
        if prefix_var in os.environ:
            prefix = os.environ[prefix_var]
            kwargs.update(
                include_dirs=[os.path.join(prefix, "include")],
                library_dirs=[os.path.join(prefix, "lib")],
                runtime_library_dirs=[os.path.join(prefix, "lib")],
            )
            cflags.append("-I" + os.path.join(prefix, "include"))

    p = subprocess.Popen(
        [cc, *cflags, "-E", "-"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = p.communicate(include_header.encode())

    if p.returncode != 0:
        raise RuntimeError(
            f"Error preprocessing header:\n{err.decode()}\n"
        )

    cdefs = out.decode()

ffibuilder = cffi.FFI()
ffibuilder.set_source("dftd3._libdftd3", include_header, **kwargs)
ffibuilder.cdef(cdefs)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
