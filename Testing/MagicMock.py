from unittest.mock import Mock, MagicMock

plain_mock = Mock()
magic_mock = MagicMock()

print(len(magic_mock))

#magic mock supports any index position
print(magic_mock[44])
print(magic_mock[200])
print(magic_mock["Hello"])