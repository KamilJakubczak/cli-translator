import pytest
from unittest.mock import patch
import requests
from main import CambridgeDictionrayDownloader


@patch('requests.get')
def test_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError()
    with pytest.raises(Exception):
        d = CambridgeDictionrayDownloader()
        d.get_translation('cat')
