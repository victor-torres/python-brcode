# python-brcode

Generates static BR Codes that could be used for PIX payments
using simple value copy and paste or generating QR Codes.

**Notes:**

Although this initial version is functional,
it's yet very simple.
We're not performing proper data validation
and the user is responsible for providing valid PIX Keys.

For example:
- email addresses should be valid
- CPF and CNPJ should contain only digits
- phone numbers should follow international patterns and begin with a + sign
- the amount should not be a negative number

**Always check the resulting codes or code generation routines before exposing them in production environments.**

Tested with Nubank, Inter, Banco do Brasil, and BTG banks. 

## Installing

```shell
pip install python-brcode
```

## Usage

### Including all parameters

```python
from decimal import Decimal
from brcode import BRCode

brcode = BRCode(
    name="Victor Torres",
    key="vpaivatorres@gmail.com",
    city="Natal",
    amount=Decimal(10.00),                    # optional
    description="Biblioteca python-brcode",   # optional
    transaction_id="***",                     # optional
)
assert str(brcode) == "00020126720014br.gov.bcb.pix0122vpaivatorres@gmail.com0224Biblioteca python-brcode520400005303986540510.005802BR5913Victor Torres6005Natal62070503***6304C1FA"
```

### Omitting optional parameters

```python
from decimal import Decimal
from brcode import BRCode

brcode = BRCode(
    name="Victor Torres",
    key="vpaivatorres@gmail.com",
    city="Natal",
)
assert str(brcode) == "00020126480014br.gov.bcb.pix0122vpaivatorres@gmail.com02005204000053039865802BR5913Victor Torres6005Natal62070503***6304A5EE"
```

## Generating QR Code

**This library does not handle QR Code generation.**

To generate a QR Code that could be scanned by most bank apps,
you should use a third-party library of your choice. 
The QR Code should be generated using the BR Code as its text.

### Example

Using the library [python-qrcode](https://github.com/lincolnloop/python-qrcode):

Install the library:

```shell
pip install qrcode
```

Generate a new BR Code and then a QR Code out of it:

```python
from decimal import Decimal
from brcode import BRCode
import qrcode

brcode = BRCode(
    name="Victor Torres",
    key="vpaivatorres@gmail.com",
    city="Natal",
)

img = qrcode.make(str(brcode))
img.save("qrcode.png")
```

![QR Code](qrcode.png)

## References

- Based on [go-pix](https://github.com/fonini/go-pix) repository
- [Regulamento PIX](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf)
