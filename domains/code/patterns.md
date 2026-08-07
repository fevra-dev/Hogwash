# Code Patterns — AI Anti-Patterns in Code

Part of domains/code/. This file is the language-level catalog: what AI-written code looks like when you read it. The other four answer different questions and are loaded separately.

- **[security.md](security.md)** — is it exploitable? A different axis from whether it reads badly, and the one with hard comparative numbers behind it.
- **[supply-chain.md](supply-chain.md)** — what does it import, and does that package exist? Now an active attack vector rather than a correctness problem.
- **[agentic.md](agentic.md)** — how was it produced? Autocomplete and an autonomous agent fail differently, and the agent failure compounds.
- **[enforcement.md](enforcement.md)** — making the rest impossible to commit, rather than catching it afterward.

**The umbrella question, shared across all five:** most of what follows is one defect class wearing different outfits, code that is *structurally plausible but functionally empty*. Placeholder code, hallucinated imports, and mock-echo tests all pass a skim; none of them do what they appear to do. Ask this question first, per file: does this actually do the thing it looks like it does, or does it just have the shape of doing it?

**Scope note on languages.** The examples below are mostly Python and TypeScript, which reflects where the source studies looked rather than where the problem is. Where a pattern is known to differ by language, it says so. The one measured difference worth carrying: in Veracode's 2026 testing across 100+ models and 80 tasks, 45% of AI-generated samples failed security tests overall, and Java failed at 72%. Language choice changes the base rate, so do not read a clean Python result as a statement about a Java codebase.

---

## CRITICAL SEVERITY — Fix before shipping

### Placeholder Code
```python
def validate_email(email):
    pass  # TODO: implement

def process():
    pass  # placeholder
```
Fix it or flag it explicitly. Never ship `pass` with a comment. The comment is a tell. It means the code was generated without being implemented.

### Mutable Default Arguments
```python
# Bug: shared state between calls
def process(items=[]):
    items.append(1)
    return items

# Fix
def process(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```

### Bare Except
```python
try:
    risky()
except:  # swallows Ctrl+C and SystemExit
    pass

# Fix: catch specific exceptions
try:
    risky()
except ValueError as e:
    logger.error("Validation failed: %s", e)
```

---

## HIGH SEVERITY

### Hedging Comments
```python
x = calculate()  # should work hopefully
result = parse()  # might need adjustment
```
Fix the uncertainty before committing. Documented doubt in comments is not a fix.

### Cross-Language Leakage
AI trained on multiple languages leaks syntax from other languages:

| Wrong | Right language | Fix |
|---|---|---|
| `.push()` | Python | `.append()` |
| `.equals()` | Python | `==` |
| `.length` | Python | `len()` |
| `.forEach()` | Python | `for` loop |
| `nil` | Python | `None` |
| `fmt.Println()` | Python | `print()` |
| `.toString()` | Python | `str()` |
| `.isEmpty()` | Python | `not obj` |
| `.ToLower()` | Python | `.lower()` |
| `var` | Modern JS/TS | `const` / `let` |

### Wrong Abstraction Tier
AI defaults to the most impressive-sounding pattern regardless of actual scale:
- Repository pattern for a simple CRUD app with one data source
- Factory class for a type that is always the same
- Plugin architecture for code that runs once
- Abstract base class with one subclass that will never have another
- Strategy pattern where the strategy never changes

Check: does this abstraction serve a real multiplicity of cases, or does it serve the appearance of sophistication?

### Type-System Workarounds (TypeScript)
- `any` casts used only to suppress type errors
- `@ts-ignore` or `@ts-expect-error` covering real type issues rather than genuine false positives
- Overly broad union types (`string | number | boolean | null | undefined`) to satisfy the compiler without fixing the actual problem

### Missing Resource Bounds in Concurrency
```python
# AI output — will exhaust connection pool or trigger rate limits
results = await asyncio.gather(*[fetch(url) for url in large_list])

# Fix: explicit semaphore
sem = asyncio.Semaphore(10)
async def bounded_fetch(url):
    async with sem:
        return await fetch(url)
results = await asyncio.gather(*[bounded_fetch(url) for url in large_list])
```

### Missing Idempotency
AI-generated POST endpoints are rarely safe to retry. If an operation might be called twice (retry on failure, webhook replay, network timeout), it needs an idempotency key or duplicate detection.

### Generic Variable Names
AI names variables generically rather than for their content.

| Generic (tell) | Better |
|---|---|
| `data` | `user_records`, `api_response`, `parsed_csv` |
| `result` | `validation_errors`, `matched_users`, `compiled_regex` |
| `temp` | `interim_score`, `swapped_value` |
| `item` | `invoice`, `user`, `config_entry` |
| `handleData()` | `normalizeUserInput()`, `parseApiResponse()` |
| `processItems()` | `deduplicateInvoices()`, `filterExpiredTokens()` |

### Hallucinated Imports
```python
from ml_utils import smart_predict  # package does not exist
import datascience as ds  # not a real library
from helper_tools import magic_function  # does not exist
```
Roughly 20% of AI-suggested package imports reference non-existent libraries. Verify every import against a real package before shipping.

**This stopped being only a correctness problem.** Attackers now register the hallucinated names, so installing one can execute their code rather than failing. See [supply-chain.md](supply-chain.md), which covers why these names are predictable enough to squat and what to do about it.

### Missing Adversarial Input Handling
AI writes for well-formed inputs. Check every public-facing function:
- Auth/permission check before data access?
- Input sanitization before database or shell operations?
- Handling of malformed/malicious input that doesn't fit the happy path?
- SQL injection protection on user-supplied values?
- Path traversal protection on user-supplied file paths?

This checklist is the reading-level version. [security.md](security.md) carries the measured defect distribution behind it, which changes what to check first: injection-class weaknesses alone account for roughly a third of confirmed vulnerabilities in AI-generated code.

---

## MEDIUM SEVERITY

### Redundant Comments
```python
# Increment x
x += 1

# Create empty list
items = []

# Return result
return result
```
Comments that restate code in English add noise without information. Delete.

### Shallow Test Coverage
AI tests the happy path. For every test, verify:
- What happens when the input is null/empty/zero?
- What happens when the external call fails?
- What boundary values (0, -1, MAX_INT) exercise different code paths?
- Does the test verify business logic, or just that arithmetic works?

**The mock echo anti-pattern** (specific to AI-generated tests):
```javascript
// AI writes this: test passes, does nothing
mock.returns(expectedValue)
expect(mock.result).toBe(expectedValue)
// You just tested that mocking works. Not the business logic.
```
ESLint rule recommendation: detect when a mock return value is directly asserted on without any intervening behavior test.

### Debug Artifacts in Committed Code
- `console.log` / `print()` / `debugger` statements
- Commented-out blocks of old code
- `// TODO` comments that are not actionable or tracked anywhere
- Magic numbers without documentation:
```python
TIMEOUT = 47  # Why 47?
RETRIES = 5   # Why 5?
# Fix: document the rationale
REQUEST_TIMEOUT = 30  # HTTP requests typically complete within 30s; longer timeout for slow connections
MAX_RETRIES = 3  # Three retries balances reliability vs speed; most failures resolve by second retry
```

### Outdated Patterns from Training Data
AI was trained on code from 2015–2023. Check for:
- `os.path` → use `pathlib` in modern Python
- `var` → `const`/`let` in modern JavaScript
- Callback patterns → `async/await` in Node.js
- `componentDidMount` → `useEffect` in React
- Any deprecated API the model's training data may not show as deprecated

### Happy-Path-Only Code
AI rarely considers failure states in generated code:
- What if the file doesn't exist?
- What if the API returns 429?
- What if the database is down?
- What if the user is unauthenticated?

The fix isn't just adding `try/except`. It's asking "what should actually happen in each failure mode?" and implementing that.

---

## Where the Other Files Pick Up

The two prevention layers that used to live here have moved, because they answer questions this file does not. Building code so the failure cannot happen is in [agentic.md](agentic.md); making it impossible to commit is in [enforcement.md](enforcement.md).

---

## Sources

sloppylint, OX Security 300+ repo analysis, CodeRabbit AI vs. human PR study 2025, Uplevel developer survey 2024, USENIX package hallucination study (arXiv:2406.10279), part of the original v2.2 skill (see SKILL.md's frontmatter for that broader source list). Veracode's 2026 language-failure-rate figures in the scope note are cited in full in security.md. The Workflow Layer that used to close this file now lives in agentic.md with its sourcing.
