"""Python wrappers for gvfs-tools bash commands"""


from pysyncdorid.utils import run_bash_cmd


def ls(path):
    """
    ls

    :argument path: target path for listing content
    :type path: str

    """
    run_bash_cmd(['gvfs-ls', path])


def mkdir(path):
    """
    mkdir -p

    NOTE: '-p' -> Create parent directories when necessary.

    :argument path: new directory path
    :type path: str

    """
    run_bash_cmd(['gvfs-mkdir', '-p', path])


def rm(src):
    """
    rm -f

    NOTE: '-f' -> Ignore nonexistent and non-deletable files.

    :argument src: file to be removed
    :type src: str

    """
    run_bash_cmd(['gvfs-rm', '-f', src])


def cp(src, dst):
    """
    cp

    :argument src: source file/directory to be copied
    :type src: str
    :argument dst: destination file/directory
    :type dst: str

    """
    run_bash_cmd(['gvfs-copy', src, dst])


def mv(src, dst):
    """
    mv

    :argument src: source file/directory to be copied
    :type src: str
    :argument dst: destination file/directory
    :type dst: str

    """
    cp(src, dst)
    rm(src)
