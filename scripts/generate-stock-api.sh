#!/bin/sh
set -eu

output=${1:?Provide a new absolute output directory}
case "$output" in
  /*) ;;
  *) echo "The output directory must be absolute" >&2; exit 1 ;;
esac
if [ -e "$output" ]; then
  echo "The output directory already exists: $output" >&2
  exit 1
fi

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
mkdir -p "$output"

buf generate --template buf.gen.yaml --output "$output"
buf generate --template buf.openapi.gen.yaml --path dictybase/stock/stock.proto --output "$output"

spec="$output/openapi/dictybase/stock/stock.openapi.json"
gateway="$output/generated/github.com/dictyBase/go-genproto/dictybaseapis/stock/stock.pb.gw.go"
python3 scripts/check_stock_api.py "$spec" "$gateway"

mkdir -p "$output/pages/openapi"
cp "$spec" "$output/pages/openapi/stock.openapi.json"
cp docs/index.html "$output/pages/index.html"
python3 scripts/test_swagger_page.py "$output/pages"
