
import argparse
import sys
import os
import shutil

from contextlib import contextmanager

try:
    from git import Repo
except ImportError:
    sys.stderr.write("This script uses GitPython. Install it ('pip install gitpython')"
                     "and try again")
    exit()


@contextmanager
def file_to_modify(filename):
    old = filename + '~'
    shutil.move(filename, old)
    with open(old, 'r') as f_old:
        with open(filename, 'w') as f_new:
            try:
                yield f_old, f_new
            except Exception as e:
                shutil.move(old, filename)
                sys.stdout.write("Restored '{!r}' to {!r}.")
                raise e


def create_branch(repo, branch_name):
    # Sanity checks
    if str(repo.active_branch) != "master":
        sys.stderr.write("This script must be launched from 'master' branch\n")
        exit()

    if repo.is_dirty():
        sys.stderr.write("Clean 'master' branch first\n")
        exit()

    # Create and checkout branch
    branch = repo.create_head(branch_name, repo.heads.master)
    repo.head.reference = branch
    assert not repo.head.is_detached
    repo.head.reset(index=True, working_tree=True)


def main(repo, version):
    create_branch(repo, version)

    # Modify files
    just_substitute = ['.travis.yml', 'appveyor.yml', 'build.py',]
    for item in just_substitute:
        print(" working on file {!r}".format(item))
        filename = os.path.join(os.path.dirname(__file__), item)
        with file_to_modify(filename) as (old, new):
            for line in old:
                new.write(line.replace("master", version))

    filename = os.path.join(os.path.dirname(__file__), 'conanfile.py')
    with file_to_modify(filename) as (old, new):
        for line in old:
            new.write(line.replace("version = \"master\"", "version = \"{}\"".format(version)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create new branch for released version.')
    parser.add_argument('release', help='name of new release: v19.20160120')
    args = parser.parse_args()

    print("="*20)
    print("Create branch for new release\n")
    print("\trelease: {!r}".format(args.release))

    repo = Repo(os.path.dirname(__file__))
    assert not repo.bare

    main(repo, args.release)

    print("Done! Now run tests and commit.")
    print("Don't forget to modify 'README.md'")
