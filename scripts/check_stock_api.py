#!/usr/bin/env python3
"""Check the generated OpenAPI and gateway routes for the stock API."""

import json
import re
import sys
from pathlib import Path


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def main():
    if len(sys.argv) != 3:
        fail("usage: check_stock_api.py OPENAPI_FILE GATEWAY_FILE")

    spec = json.loads(Path(sys.argv[1]).read_text())
    if spec.get("openapi") != "3.1.0":
        fail("unexpected OpenAPI version")
    paths = spec.get("paths", {})
    if set(paths) != {"/v1/stocks/counts"} or set(paths["/v1/stocks/counts"]) != {"get"}:
        fail("unexpected OpenAPI routes")

    gateway = Path(sys.argv[2]).read_text()
    registrations = re.findall(r"mux\.Handle\((http\.Method\w+),\s*(\w+)\s*,", gateway)
    expected = ("http.MethodGet", "pattern_StockService_CountStocks_0")
    if registrations != [expected, expected] or gateway.count("mux.Handle(") != 2 or "mux.HandlePath(" in gateway:
        fail("unexpected gateway registrations")

    pattern = (
        r'pattern_StockService_CountStocks_0\s*=\s*runtime\.MustPattern\('
        r'runtime\.NewPattern\(1,\s*\[\]int\{2,\s*0,\s*2,\s*1,\s*2,\s*2\},\s*'
        r'\[\]string\{"v1",\s*"stocks",\s*"counts"\},\s*""\)\)'
    )
    if len(re.findall(pattern, gateway)) != 1:
        fail("unexpected gateway path")
    print("Stock API contract matches GET /v1/stocks/counts")


if __name__ == "__main__":
    main()
