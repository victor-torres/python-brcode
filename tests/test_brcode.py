from decimal import Decimal

from brcode import BRCode

import pytest


@pytest.mark.parametrize(
    ("input_data", "brcode_string"),
    (
        (
            dict(
                name="Victor Torres",
                key="vpaivatorres@gmail.com",
                city="Natal",
                amount=Decimal(10.00),                    # optional
                description="Biblioteca python-brcode",   # optional
                transaction_id="***",                     # optional
            ),
            "00020126720014br.gov.bcb.pix0122vpaivatorres@gmail.com0224Biblioteca python-brcode520400005303986540510.005802BR5913Victor Torres6005Natal62070503***6304C1FA",
        ),
        (
            dict(
                name="Victor Torres",
                key="vpaivatorres@gmail.com",
                city="Natal",
            ),
            "00020126480014br.gov.bcb.pix0122vpaivatorres@gmail.com02005204000053039865802BR5913Victor Torres6005Natal62070503***6304A5EE",
        )
    ),
)
def test_brcode(input_data: dict[str, str | Decimal], brcode_string):
    brcode = BRCode(**input_data)
    assert str(brcode) == brcode_string
