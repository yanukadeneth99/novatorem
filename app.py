"""
Vercel Flask-preset entrypoint.

Vercel's Flask backend preset auto-discovers the WSGI app by looking for
`app.py` / `main.py` / `index.py` at the repo root. The real application
lives in `api/orchestrator.py`; this module just re-exports it so the
preset's detector can find it without renaming the canonical module.
"""

from api.orchestrator import app

__all__ = ["app"]
