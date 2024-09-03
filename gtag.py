#!/usr/bin/env python3
import semantic_version
import subprocess
import os

def main(message, major, minor, patch):
    os.chdir(os.getcwd())
    repo_dir = os.path.basename(os.getcwd())
    if not message:
        p = subprocess.Popen("git log -1 --pretty=%B", shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        message = str(out.decode('utf-8')).rstrip("\n")

    p = subprocess.Popen("git fetch", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = p.communicate()
    p = subprocess.Popen("git tag --list | sort", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = p.communicate()
    try:
        versions = list()
        for x in str(out.decode('utf-8')).splitlines():
            try:
                versions.append(semantic_version.Version(x.lstrip("v")))
            except ValueError:
                continue
            last_version = sorted(versions).pop()
    except IndexError:
        last_version = semantic_version.Version("0.0.0")
    except UnboundLocalError:
        last_version = semantic_version.Version("0.0.0")
    try:
        if patch:
            next_version = str(last_version.next_patch())
        if minor:
            next_version = str(last_version.next_minor())
        if major:
            next_version = str(last_version.next_major())
    except UnboundLocalError:
        next_version = semantic_version.Version("0.0.1")
    print(next_version)
    # p = subprocess.Popen(f"git tag -a {next_version} -m '{message}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, _ = p.communicate()
    # print("Pushing tags...")
    # p = subprocess.Popen("git push --tags", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, _ = p.communicate()

if __name__ == '__main__':
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-m", dest="message")
    p.add_option("--patch", dest="patch", default=True, action="store_true")
    p.add_option("--minor", dest="minor", default=False, action="store_true")
    p.add_option("--major", dest="major", default=False, action="store_true")
    opt, args = p.parse_args()
    main(opt.message, opt.major, opt.minor, opt.patch)

