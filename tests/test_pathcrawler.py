from pathlib import Path

import pytest

import pathcrawler


def test_pathcrawler_crawl():
    paths = pathcrawler.crawl(Path(__file__).parent.parent)
    file_names = [path.name for path in paths]
    for name in [
        "__init__.py",
        "pathcrawler.py",
        "test_pathcrawler.py",
        "README.md",
        "pyproject.toml",
        "LICENSE.txt",
    ]:
        assert name in file_names


def test_pathcrawler_get_directory_size():
    assert pathcrawler.get_directory_size(Path(__file__).parent.parent) > 1


@pytest.mark.parametrize(
    "size,expected",
    [
        (1234, "1.23 kb"),
        (32, "32 bytes"),
        (17728349, "17.73 mb"),
        (837199281928, "837.2 gb"),
    ],
)
def test_pathcrawler_format_size(size, expected):
    assert pathcrawler.format_size(size) == expected
