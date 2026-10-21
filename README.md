# cscModule8 — CSC 325 Module 8: First CI/CD Pipeline

A small Django + Django REST Framework backend with a four-stage GitHub Actions
CI/CD pipeline, built by following the Module 8 tutorial (same project layout as
`csc325DjangoProject`: Django project `csc325DjangoProject`, app `myapp`).

## Endpoints

| URL | What it returns |
|---|---|
| `/` | Home page (HTML greeting) |
| `/about/` | About page (HTML) |
| `/api/hello/` | REST API endpoint — JSON: `{"message": "Hello, World!", "status": "ok"}` |

## Tests

Three automated tests in `myapp/tests.py` (home page, about page, API endpoint).
Run them locally with:

```
pip install -r requirements.txt
python manage.py test
```

A failing test fails the pipeline — the Deploy stage cannot run unless Test passes.

## Pipeline — `.github/workflows/csc325_ci_cd.yml`

Runs automatically on every push to `main`, in four stages:

1. **Setup** — checks out the code and installs Python 3.8 (the tutorial version)
2. **Install Dependencies** — installs the packages from `requirements.txt`
3. **Test** — runs the full test suite (`python manage.py test`)
4. **Deploy** — deploys the application; it declares `needs: test`, so GitHub
   Actions will not start it until the Test stage has finished green

## Branches

- `main` — protected by a ruleset
- `feature/add-status-endpoint` — feature branch for new work
