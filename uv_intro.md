# ⚙️ `uv` — The Fast Python Toolchain by Astral

`uv` is a **next-generation Python package manager and environment tool**, developed by **Astral**, designed to **replace multiple tools like `pip`, `venv`, and `pipx`** — all combined into one ultra-fast binary (written in Rust).

It’s similar to what **npm** is for Node.js or **cargo** is for Rust, but for **Python**.

---

## 🧰 Main Uses of `uv`

| Category | Description | Example |
|-----------|--------------|----------|
| 🐍 **Environment Management** | Create and manage virtual environments (like `venv` or `virtualenv`) | `uv venv`<br>`uv run` |
| 📦 **Package Management** | Install, update, or remove Python packages (replaces `pip`) | `uv add requests`<br>`uv remove numpy` |
| ⚡ **Fast Package Installer** | Installs packages much faster than pip (thanks to Rust backend) | `uv pip install flask` |
| 🧑‍💻 **Python Runner** | Run Python scripts directly in isolated environments | `uv run script.py` |
| 🌐 **Project Dependency Resolver** | Resolves dependencies using lockfiles (`uv.lock`) for reproducible builds | `uv lock`<br>`uv sync` |
| 🧱 **Package Building & Publishing** | Build and publish Python packages (like `build` + `twine`) | `uv build`<br>`uv publish` |
| 🧩 **pipx-like App Runner** | Run CLI tools in ephemeral environments (like `pipx run`) | `uv tool run black` |
| 🔄 **Cross-version Python Management** | Manage and isolate multiple Python versions automatically | `uv python install 3.12` |
| 🧠 **Caching & Offline Installs** | Smart caching enables offline installations | — |

---

## 🚀 Why Developers Use `uv`

✅ **Much faster** than pip (built in Rust)  
✅ **One tool replaces many** (`pip`, `venv`, `pipx`, `build`, etc.)  
✅ **Clean environment management** — both local and global  
✅ **Reproducible builds** with `uv.lock`  
✅ **Fully compatible** with `requirements.txt` and `pyproject.toml`

---

## 💻 Common Commands

| Command | Purpose |
|----------|----------|
| `uv init` | Initialize a new Python project |
| `uv add <package>` | Install and add a package to dependencies |
| `uv remove <package>` | Uninstall a package |
| `uv run <file.py>` | Run a script in a managed virtual environment |
| `uv sync` | Install all dependencies from `pyproject.toml` |
| `uv pip install <pkg>` | Use pip-style installation (for compatibility) |
| `uv build` | Build your Python package |
| `uv publish` | Publish your package to PyPI |
| `uv tool run <cli>` | Run Python CLI apps in ephemeral environments |
| `uv python install 3.12` | Manage and install specific Python versions |

---

## 🧩 Tool Comparison

| Traditional Tool | Replaced by `uv` |
|------------------|------------------|
| `pip` | ✅ `uv pip` |
| `virtualenv` / `venv` | ✅ `uv venv` |
| `pipx` | ✅ `uv tool run` |
| `poetry` / `pipenv` | ⚙️ Partially replaced — similar lockfile features |
| `build` / `twine` | ✅ `uv build`, `uv publish` |

---

## ⚡ Example Workflow

```bash
# 1️⃣ Initialize a new project
uv init myproject
cd myproject

# 2️⃣ Add dependencies
uv add flask

# 3️⃣ Run your Python app
uv run app.py

# 4️⃣ Sync dependencies from lockfile
uv sync

# 5️⃣ Build and publish your package
uv build
uv publish



# Comparison: `uv` vs `pip`

`uv` and `pip` are both tools used in the Python ecosystem, but they serve **different purposes** and have different features. This document compares them clearly.

---

## 1. **Overview**

| Tool | Description |
|------|-------------|
| **pip** | The default Python package installer. Installs Python packages from PyPI and manages dependencies. |
| **uv**  | A modern, all-in-one Python toolchain (by Astral) that manages packages, virtual environments, Python versions, and CLI tools. Written in Rust for speed. |

---

## 2. **Key Differences**

| Feature | pip | uv |
|---------|-----|----|
| **Primary Function** | Install, update, and uninstall Python packages | Manage Python packages, virtual environments, dependencies, and run scripts |
| **Environment Management** | None (relies on `venv` or `virtualenv`) | Built-in environment management (`uv venv`) |
| **Dependency Locking** | No built-in lockfile (pip can use `requirements.txt`) | Uses `uv.lock` for reproducible environments |
| **Package Installation Speed** | Standard Python speed | Very fast (Rust backend) |
| **Python Version Management** | No | Built-in (`uv python install 3.12`) |
| **CLI Tool Execution** | No | Yes (`uv tool run <cli>`) similar to pipx |
| **Project Setup** | No | Yes, can initialize projects with `uv init` |
| **Integration with pyproject.toml** | Partial (via requirements.txt) | Full integration, auto-updates dependencies |
| **Reproducible Builds** | Manual (`requirements.txt`) | Automatic using `uv.lock` |

---

## 3. **When to Use Each**

| Use Case | Recommended Tool |
|----------|-----------------|
| Install a single Python package | `pip install <package>` |
| Manage multiple Python projects with isolated environments | `uv` |
| Run a Python CLI tool in an isolated environment | `uv tool run <cli>` |
| Ensure reproducible builds with dependency lockfile | `uv` |
| Quick, simple package installation | `pip` |

---

## 4. **Example Commands**

### pip
```bash
pip install requests
pip uninstall requests
pip freeze > requirements.txt
