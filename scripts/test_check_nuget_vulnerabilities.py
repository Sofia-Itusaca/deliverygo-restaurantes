import json
import tempfile
import unittest
from pathlib import Path

from check_nuget_vulnerabilities import main


class NuGetAuditTests(unittest.TestCase):
    def run_report(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return main(path)

    def test_no_findings_passes(self):
        self.assertEqual(self.run_report({"version": 1, "projects": []}), 0)

    def test_low_finding_passes(self):
        report = {"projects": [{"packages": [{"vulnerabilities": [{"severity": "Low"}]}]}]}
        self.assertEqual(self.run_report(report), 0)

    def test_high_or_critical_fails(self):
        for severity in ("High", "Critical"):
            with self.subTest(severity=severity):
                report = {"projects": [{"packages": [{"vulnerabilities": [{"severity": severity}]}]}]}
                self.assertEqual(self.run_report(report), 1)

    def test_unclassified_finding_fails_closed(self):
        report = {"projects": [{"packages": [{"vulnerabilities": [{"advisoryUrl": "https://example.invalid"}]}]}]}
        self.assertEqual(self.run_report(report), 1)


if __name__ == "__main__":
    unittest.main()
