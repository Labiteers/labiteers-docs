# [<img src="source/_static/logo.jpg" alt="Labiteers Logo" width="25" style="vertical-align: -8px; margin-right: 10px;">](https://docs.labiteers.com) Labiteers Documentation

This repository contains the official documentation for **Labiteers Ltd.**’s SaaS platform.  
You can view the live version at [**docs.labiteers.com**](https://docs.labiteers.com).

---

## 📁 Structure

- `source/` – The Sphinx source files (`.rst`, `_static`, `_templates`, etc.)
- `build/` – Auto-generated build output (ignored in Git)

---

## 🛠️ Building the Docs Locally

### On Linux/macOS:
```bash
make html
```

```bash
sphinx-autobuild source build/html
```
