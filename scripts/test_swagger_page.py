import json
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PAGES = Path(sys.argv.pop(1)) if len(sys.argv) > 1 else ROOT / "docs"
ARTIFACT = PAGES != ROOT / "docs"
CDN = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.18.2/"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class SwaggerPageTest(unittest.TestCase):
    def page(self):
        page = PAGES / "index.html"
        self.assertTrue(page.is_file(), f"missing Swagger UI page: {page}")
        return page.read_text()

    def test_page_loads_pinned_swagger_assets(self):
        parser = PageParser()
        parser.feed(self.page())
        self.assertIn(("link", {"rel": "stylesheet", "href": CDN + "swagger-ui.css"}), parser.elements)
        self.assertIn(("script", {"src": CDN + "swagger-ui-bundle.js"}), parser.elements)
        self.assertIn(("div", {"id": "swagger-ui"}), parser.elements)

    def test_page_loads_the_local_spec(self):
        self.assertRegex(self.page(), r'url:\s*["\']\./openapi/stock\.openapi\.json["\']')

    def test_page_disables_external_validator_and_api_calls(self):
        page = self.page()
        self.assertRegex(page, r"validatorUrl:\s*null")
        self.assertRegex(page, r"supportedSubmitMethods:\s*\[\s*\]")

    @unittest.skipUnless(ARTIFACT, "artifact directory not supplied")
    def test_artifact_contains_the_spec(self):
        spec = PAGES / "openapi" / "stock.openapi.json"
        self.assertTrue(spec.is_file(), f"missing specification: {spec}")
        data = json.loads(spec.read_text())
        self.assertEqual(data.get("openapi"), "3.1.0")
        self.assertEqual(set(data.get("paths", {})), {"/v1/stocks/counts"})


if __name__ == "__main__":
    unittest.main()
