import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).with_name("check_stock_api.py")
GATEWAY = '''
func register(mux *runtime.ServeMux) {
    mux.Handle(http.MethodGet, pattern_StockService_CountStocks_0, handler)
    mux.Handle(http.MethodGet, pattern_StockService_CountStocks_0, handler)
}
var pattern_StockService_CountStocks_0 = runtime.MustPattern(runtime.NewPattern(1, []int{2, 0, 2, 1, 2, 2}, []string{"v1", "stocks", "counts"}, ""))
'''


class StockAPIContractTest(unittest.TestCase):
    def check_contract(self, spec, gateway=GATEWAY):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            spec_path = root / "stock.openapi.json"
            gateway_path = root / "stock.pb.gw.go"
            spec_path.write_text(json.dumps(spec))
            gateway_path.write_text(gateway)
            return subprocess.run(
                [sys.executable, str(CHECKER), str(spec_path), str(gateway_path)],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_accepts_only_count_stocks(self):
        result = self.check_contract({"openapi": "3.1.0", "paths": {"/v1/stocks/counts": {"get": {}}}})
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_wrong_openapi_version(self):
        result = self.check_contract({"openapi": "3.0.0", "paths": {"/v1/stocks/counts": {"get": {}}}})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("OpenAPI version", result.stderr)

    def test_rejects_extra_openapi_operation(self):
        result = self.check_contract({"openapi": "3.1.0", "paths": {"/v1/stocks/counts": {"get": {}, "post": {}}}})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("OpenAPI routes", result.stderr)

    def test_rejects_missing_openapi_route(self):
        result = self.check_contract({"openapi": "3.1.0", "paths": {}})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("OpenAPI routes", result.stderr)

    def test_rejects_wrong_http_method(self):
        result = self.check_contract({"openapi": "3.1.0", "paths": {"/v1/stocks/counts": {"post": {}}}})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("OpenAPI routes", result.stderr)

    def test_rejects_extra_gateway_route(self):
        gateway = GATEWAY + '\nmux.Handle(http.MethodPost, pattern_StockService_CreateStrain_0, handler)\n'
        result = self.check_contract({"openapi": "3.1.0", "paths": {"/v1/stocks/counts": {"get": {}}}}, gateway)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gateway registrations", result.stderr)

    def test_rejects_wrong_gateway_path(self):
        gateway = GATEWAY.replace('"counts"', '"other"')
        result = self.check_contract({"openapi": "3.1.0", "paths": {"/v1/stocks/counts": {"get": {}}}}, gateway)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gateway path", result.stderr)


if __name__ == "__main__":
    unittest.main()
