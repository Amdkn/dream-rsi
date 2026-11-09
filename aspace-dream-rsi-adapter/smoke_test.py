"""Smoke test de l'adapter A'Space pour dream-rsi (contrat seul).

Hors-ligne : --help de la CLI + import du paquet. Aucun appel modèle,
aucun appel réseau, aucune tâche KernelBench.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GEL = "8ec35bd"


def _git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args],
                          capture_output=True, text=True,
                          check=True).stdout.strip()


def test_gel_is_ancestor():
    assert _git("merge-base", "HEAD", GEL) == _git("rev-parse", GEL)


def test_only_adapter_changed():
    out = _git("diff", "--name-only", GEL, "HEAD")
    assert out, "aucun fichier changé depuis le gel"
    assert all(p.startswith("aspace-dream-rsi-adapter/")
               for p in out.splitlines())


def test_contract():
    c = json.loads((HERE / "contract.json").read_text())
    assert c["upstream"]["frozen_commit"] == GEL
    assert c["version"] == "0.1.0"


def test_package_imports_offline():
    sys.path.insert(0, str(ROOT))
    import dream_rsi
    from dream_rsi.cli.main import main
    assert callable(main)


def test_cli_help():
    p = subprocess.run([sys.executable, "-m", "dream_rsi", "--help"],
                       capture_output=True, text=True, timeout=60,
                       cwd=str(ROOT))
    assert p.returncode == 0
    assert "learning" in p.stdout
    assert "explore" in p.stdout
