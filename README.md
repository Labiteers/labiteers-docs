# [<img src="source/_static/logo.jpg" alt="Labiteers Logo" width="100" style="vertical-align: -8px; margin-right: 10px;">](https://docs.labiteers.com) Labiteers Documentation

<!-- # [<img src="source/_static/logo.jpg" alt="Labiteers Logo" width="100" style="vertical-align: -58px; margin-right: 10px;">](https://docs.labiteers.com) Labiteers Documentation -->

<!-- <h1>
  <a href="https://docs.labiteers.com" style="text-decoration: none;">
    <img src="source/_static/logo.jpg" alt="Labiteers Logo" width="50" style="vertical-align: middle; position: relative; top: 5px; margin-right: 10px;">
  </a>
  Labiteers Documentation
</h1> -->

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
