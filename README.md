# email-auth-results-checker

Read an Authentication-Results header and report SPF, DKIM and DMARC as pass, fail or not found — trusted only when all three pass.

## How to run

```sh
python3 main.py --header "spf=pass dkim=fail dmarc=pass"
```

## Example output

```
SPF: PASS
DKIM: FAIL
DMARC: PASS
Verdict: NOT TRUSTED
```

Standard library only. Run the tests with `python3 -m unittest discover`.
