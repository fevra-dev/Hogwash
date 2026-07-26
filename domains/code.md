# Code Patterns — AI Anti-Patterns in Code

Synthesized from sloppylint, OX Security 300+ repo analysis, CodeRabbit AI vs. human PR study 2025, Uplevel developer survey 2024, USENIX package hallucination study (arXiv:2406.10279), and aihero.dev's "Tracer Bullets" article (2026, applying a technique from *The Pragmatic Programmer* to AI agent workflows specifically).

**The umbrella question:** most of what follows is one defect class wearing different outfits, code that is *structurally plausible but functionally empty*. Placeholder code, hallucinated imports, and mock-echo tests all pass a skim; none of them do what they appear to do. Ask this question first, per file: does this actually do the thing it looks like it does, or does it just have the shape of doing it?

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
~20% of AI-suggested package imports reference non-existent libraries (USENIX study arXiv:2406.10279). Verify every import against a real package before shipping.

### Missing Adversarial Input Handling
AI writes for well-formed inputs. Check every public-facing function:
- Auth/permission check before data access?
- Input sanitization before database or shell operations?
- Handling of malformed/malicious input that doesn't fit the happy path?
- SQL injection protection on user-supplied values?
- Path traversal protection on user-supplied file paths?

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

## THE WORKFLOW LAYER: TRACER BULLETS

A second prevention layer, different in kind from the Enforcement Layer below: that one blocks bad code from being committed, this one changes how the code gets built in the first place, before there's anything to commit or catch.

**Why this connects to the umbrella question above.** Left unconstrained, an agent tends to build every horizontal layer of a feature (models, endpoints, middleware, auth, logging) before ever testing whether the critical path works at all. Only after all of it exists does anyone discover the database connection string was wrong, or the column type didn't match. That's not a coincidence, it's the direct mechanism behind structurally-plausible-but-functionally-empty code: a large, complete-looking deliverable with an untested core, built in the dark with no feedback loop until the very end.

**The fix, borrowed from a much older idea.** *The Pragmatic Programmer* calls this failure mode "outrunning your headlights," building faster than your feedback loop can catch you. Its own answer, tracer bullets, is a small, end-to-end vertical slice: one path through every layer the feature touches, working and tested, before any of the layers get built out further. Asked to add a "reveal in file system" action available from four different places in an app, the tracer-bullet version is the backend endpoint wired to exactly one of those four locations first, confirmed working, then expanded to the rest, not all four UI locations and the endpoint built simultaneously and tested at the end.

**Why this bites harder with agents than with a human developer.** A human notices when they've been coding for an hour without running anything. An agent doesn't have that instinct, and a full context window makes the discipline non-negotiable rather than just good practice: by the time something this large fails, there's no budget left to meaningfully backtrack.

**Practical instruction, for a build-feature prompt or skill:** when a feature touches multiple layers or multiple integration points, name the smallest end-to-end slice explicitly and ask for that first, tested, before any expansion. "Build the one thing that proves the hard part works" beats "build the whole feature" as an opening instruction almost every time.

## THE ENFORCEMENT LAYER (from Bootoshi)

Wordlists are advisory. ESLint/Ruff rules are structural. Build both layers.

The mock echo pattern, bare except, and `console.log` in production can all be made impossible to commit with a custom lint rule. An agent hits a lint error and must write something real. This is categorically more reliable than a post-hoc audit.

Recommended candidates for custom lint rules in your codebase:
1. Mock echo pattern (test file linter)
2. `@ts-ignore` without explanation comment
3. `console.log` in non-test files
4. `any` type without explanation comment
5. Empty `except` blocks
6. Functions longer than N lines without documentation

---

## Sources

sloppylint, OX Security 300+ repo analysis, CodeRabbit AI vs. human PR study 2025, Uplevel developer survey 2024, USENIX package hallucination study (arXiv:2406.10279), part of the original v2.2 skill (see SKILL.md's frontmatter for that broader source list). The Workflow Layer above is separately sourced: aihero.dev's "Tracer Bullets" article (2026), itself applying a technique from *The Pragmatic Programmer* to AI agent workflows specifically.
