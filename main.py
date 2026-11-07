"""Check SPF/DKIM/DMARC results in an Authentication-Results header.

Usage: python3 main.py --header "spf=pass dkim=fail dmarc=pass"
Each of spf, dkim, dmarc is reported PASS/FAIL/NOT FOUND.
TRUSTED only when all three pass.
"""
import argparse, re, sys

METHODS = ("spf", "dkim", "dmarc")

def check(header):
    results = {}
    for method in METHODS:
        m = re.search(rf"{method}=(\w+)", header.lower())
        results[method] = m.group(1).upper() if m else "NOT FOUND"
    trusted = all(results[m] == "PASS" for m in METHODS)
    return results, trusted

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--header", required=True)
    args = parser.parse_args(argv)
    results, trusted = check(args.header)
    for method in METHODS:
        print(f"{method.upper()}: {results[method]}")
    print("Verdict: " + ("TRUSTED" if trusted else "NOT TRUSTED"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
