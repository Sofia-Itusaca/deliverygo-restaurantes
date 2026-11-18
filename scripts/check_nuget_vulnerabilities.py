"""Fail CI when NuGet reports HIGH or CRITICAL package advisories."""

import json
import sys
from pathlib import Path


BLOCKING = {"HIGH", "CRITICAL"}


def walk(node):
    if isinstance(node, dict):
        if isinstance(node.get("vulnerabilities"), list):
            for advisory in node["vulnerabilities"]:
                if isinstance(advisory, dict):
                    yield advisory
        for value in node.values():
            yield from walk(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk(value)


def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    advisories = list(walk(data))
    blocking = []
    for advisory in advisories:
        severity = str(advisory.get("severity", "")).upper()
        if not severity:
            blocking.append(advisory)
        elif severity in BLOCKING:
            blocking.append(advisory)
    if blocking:
        for advisory in blocking:
            print(json.dumps(advisory, sort_keys=True))
        print(f"NuGet audit failed: {len(blocking)} HIGH/CRITICAL or unclassified advisory(ies).", file=sys.stderr)
        return 1
    print(f"NuGet audit passed: {len(advisories)} advisory(ies), none HIGH/CRITICAL.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_nuget_vulnerabilities.py <dotnet-list-json>")
    raise SystemExit(main(sys.argv[1]))
