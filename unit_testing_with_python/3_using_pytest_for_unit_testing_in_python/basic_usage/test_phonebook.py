import pytest

from .phonebook import Phonebook


# @pytest.skip('WIP')，报错
# Using pytest.skip outside of a test is not allowed. To decorate a test function, use the @pytest.mark.skip or
# @pytest.mark.skipif decorators instead, and to skip a module use `pytestmark = pytest.mark.{skip,skipif}.
def test_lookup_entry():
    # pytest.skip('WIP')
    phonebook = Phonebook()
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")


def test_phonebook_gives_access_to_names_and_numbers():
    phonebook = Phonebook()
    phonebook.add('Alice', '12345')
    assert 'Alice' in phonebook.names()
    assert '12345' in phonebook.numbers()


def test_missing_entry_raises_keyerror():
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup('missing')
