from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from brcode.crc import crc16


@dataclass(frozen=True)
class BRCode(object):
    """Generates Brazilian PIX copy and paste BR codes or QR codes."""

    key: str
    name: str
    city: str
    amount: Optional[Decimal] = None
    description: Optional[str] = None
    transaction_id: Optional[str] = None

    def __str__(self) -> str:
        """Returns string formatted BR code."""
        data_map = self._build_data_map()
        parsed_data = self._parse_data(data_map)

        # Calculate CRC16 hash
        parsed_data = parsed_data[:-4]              # Remove CRC16 placeholder
        crc = crc16(parsed_data.encode("utf-8"))    # Calculate new hash
        parsed_data += f"{crc:04x}".upper()         # Append new CRC16 value

        return parsed_data

    def _build_data_map(self) -> dict:
        """Builds internal data structure to represent BR Code."""
        data_map = {
            "00": "01",
            "26": {
                "00": "br.gov.bcb.pix",
                "01": self.key,
                "02": "" if self.description is None else self.description,
            },
            "52": "0000",
            "53": "986",
            "54": self.amount,
            "58": "BR",
            "59": self.name,
            "60": self.city,
            "62": {
                "05": "***" if self.transaction_id is None else self.transaction_id,
            },
            "63": "****",  # CRC16 placeholder
        }

        # Remove payment amount if not defined
        if data_map["54"] is None:
            data_map.pop("54")

        return data_map

    def _parse_data(self, data: dict) -> str:
        """Recursively parses internal data structure into a result string."""
        result = []

        for key, value in data.items():
            # Format numbers with two decimal places
            if isinstance(value, str):
                content = value
            elif isinstance(value, Decimal):
                content = f"{value:.2f}"
            elif isinstance(value, dict):
                content = self._parse_data(value)
            else:
                raise TypeError(f"Unsupported type {type(value)!r} for key {key!r}.")

            content_length = f"{len(content):02d}"

            result.append(key)
            result.append(content_length)
            result.append(content)

        return "".join(result)
