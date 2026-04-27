import pytest
from unittest.mock import patch, MagicMock
from main import format_product

def test_format_product_logic():
    mock_product =MagicMock()
    mock_product.pk="test-id-123"
    mock_product.name="Plazma keks"
    mock_product.price=150.0
    mock_product.quantity=200

    with patch('main.Product.get') as mocked_get :

        mocked_get.return_value = mock_product

        rezultat =format_product("test-id-123")

        assert rezultat['id']=='test-id-123'
        assert rezultat['name']=="Plazma keks"
        assert rezultat['price']==150.0
        assert rezultat['quantity']==200

        mocked_get.assert_called_once_with('test-id-123')