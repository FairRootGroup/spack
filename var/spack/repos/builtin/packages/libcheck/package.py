# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libcheck(CMakePackage):
    """A unit testing framework for C."""

    homepage = "https://libcheck.github.io/check/index.html"
    url      = "https://github.com/libcheck/check/releases/download/0.12.0/check-0.12.0.tar.gz"

    version('0.12.0', sha256='464201098bee00e90f5c4bdfa94a5d3ead8d641f9025b560a27755a83b824234')
    version('0.11.0', sha256='24f7a48aae6b74755bcbe964ce8bc7240f6ced2141f8d9cf480bc3b3de0d5616')
    version('0.10.0', sha256='f5f50766aa6f8fe5a2df752666ca01a950add45079aa06416b83765b1cf71052')