from __future__ import annotations

from dataclasses import dataclass

import firefly as ff


@dataclass
class Address:
    street_address: str = ff.required()
    locality: str = ff.required()
    region: str = ff.required()
    postal_code: str = ff.required()
    country: str = ff.required()
    formatted: str = ff.optional()
