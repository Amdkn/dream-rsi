# aspace-dream-rsi-adapter

Adapter A'Space pour `dream-rsi` (DREAM-RSI, Google Research) — gel `8ec35bd`.

**Contrat seul** (§1.5) : aucune couture spécifique. La surface exposée est
la CLI amont, section hors-ligne :

- `dream-rsi --help` / `dream-rsi learning <sous-commande>` — replay,
  export, allocate, discover, directions (hors-ligne).

**Jamais** : `dream-rsi explore` / `evolve` (agent de codage réel,
appels API), les évaluateurs KernelBench (requêtes POST vers un serveur
GPU), tout appel réseau.

**Télémétrie** : aucun SDK ; zéro appel réseau dans le paquet
(voir `dream-rsi-TELEMETRY-AUDIT.md`).

Smoke test : `pytest aspace-dream-rsi-adapter/smoke_test.py -q`
(5 tests, hors-ligne).
