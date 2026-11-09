# SCRIBE

```> A terminal-native runtime for computational notebooks. 
```
Scribe is an experimental developer tool for working with the JUPYTER NOTEBOOKS directly from the terminal.
The goal is to provide the clean, interactive, terminal-first notebook experience with cell-by-cell execution, persistence
kernel state, rich output rendering, and the future integration with the NEOVIM.

## VISION

Jupyter notebooks are powerful, but they are primarily designed around the browser-based interfaces.
Scribe explores a different approach:
```> What if notebooks could be explored, executed, and managed naturally from the terminal?
```

Scribe aims to provide a notebook runtime that works without requiring a traditional web interfaces.

### Planned Features
- Load and inspect .ipynb notebooks
- Navigate notebook cells
- Execute cells individually
- Maintain persistent kernel state
- Capture and render execution output
- execute entire notebooks
- Save execution results back to notebooks
- Terminal-native interactive interface
- Docker-based execution environments
- Neovim integration
- Experimental support for additional computational runtimes

### EXPECTED TECH STACK
- **Python** : Notebook parsing and Jupyter kernel integration
- **Rust** : Future terminal UI and native tooling
- **LUA** : Neovim integration
- **Docker** : Reproducible and isolated execution environments

### STATUS
> [!NOTE]
>Scribe is currently in the initial development phase.
>The first milestone is to build a reliable notebook loader and execution engine before adding the terminal UI or editor integrations.
