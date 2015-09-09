"""Test name creation."""
import pytest

from returns.returns import underscore_separated_words_to_camel_case


@pytest.mark.parametrize('underscore_words, expected_output', [
    ('create_sth', 'CreateSth'),
    ('create_sth_more', 'CreateSthMore'),
    ('SendMoreMoney', 'SendMoreMoney'),
    ('Send_More_Money', 'SendMoreMoney'),
    ('to_UTF_8', 'ToUTF8'),
])
def test_underscore_separated_words_to_camel_case(underscore_words, expected_output):
    """Test if underscores are removed and words are capitalized."""
    assert underscore_separated_words_to_camel_case(underscore_words) == expected_output
