# Tasks
1. Review the GitHub Actions workflow in `.github/workflows/detection-validation.yml`.
2. Run `python scripts/utilities/validate_repo.py` locally. Verify all YAML files pass.
3. Intentionally introduce a syntax error in a test rule and observe the linter fail.
4. Correct the rule and verify the exit code returns 0.
5. Document how Detection-as-Code eliminates alert drift and unmonitored regressions.
