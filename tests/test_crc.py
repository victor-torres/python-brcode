from brcode.crc import crc16

import pytest


@pytest.mark.parametrize(
    ("input_data", "output_hash"),
    (
        (
            b"00020126580014br.gov.bcb.pix0136123e4567-e12b-12d1-a456-4266554400005204000053039865802BR5913Fulano de Tal6008BRASILIA62070503***6304",
            0x1d3d,
        ),
    ),
)
def test_crc16(input_data: bytes, output_hash: int):
    assert crc16(input_data) == output_hash
