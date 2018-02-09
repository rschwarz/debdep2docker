#! /usr/bin/env python
#
# Generate a Dockerfile to provide the dependecies from .deb package files.

import subprocess

def query_deps(filename):
    """Query the Depend field of a .deb file"""
    cmd = ["dpkg-query", "-f", filename, "Depend"]
    res = subprocess.run(cmd, stdout=subprocess.PIPE)
    return res.stdout

def parse_deps(deps_str):
    """Extract list of package names from raw field string"""
    pkgs = []
    for dep in deps_str.split(','):
        dep = dep.strip()            # rm whitespace
        if dep:
            pkgs.append(dep.split()[0])  # ignore version req.
    return pkgs

def get_deps(filename):
    """List of packages from .deb files."""
    return parse_deps(query_deps(filename))
