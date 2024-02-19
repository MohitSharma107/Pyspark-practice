from Python.simplify_path import simplifyPath


def test_simplyfy_path():
    # Test case with a valid path
    assert simplifyPath("/a/b/c/../d/e/f") == "/a/b/d/e/f"

    # Test case with an empty path
    assert simplifyPath("") == "/"

    # Test case with a path containing only one directory
    assert simplifyPath("/abc") == "/abc"

    # Test case with a path containing only one directory and ".."
    assert simplifyPath("/abc/..") == "/"

    # Test case with a path containing multiple ".." directories
    assert simplifyPath("/a/b/c/../../../x/y/z") == "/x/y/z"

    # Test case with a path containing "." directories
    assert simplifyPath("/a/./b/./c") == "/a/b/c"

    print("All test cases passed!")

test_simplyfy_path()