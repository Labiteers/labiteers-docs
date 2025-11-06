# Labiteers Documentation

This repository contains the official documentation for Labiteers' SaaS platform.

## Structure

- `source/` – The Sphinx source files (`.rst`, `_static`, `_templates`, etc.)
- `build/` – Auto-generated build output (ignored in Git)

## Building the Docs Locally

### On Linux/macOS:
```bash
make html
```

```bash
sphinx-autobuild source build/html
```
