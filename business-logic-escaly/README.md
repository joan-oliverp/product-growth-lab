# Escaly — Business Logic

This folder defines **Escaly’s product business logic**: the North Star, AARRR funnel, and key metrics.  

It is intentionally **decoupled from the tracking plan**:

- **Business logic = what matters**  
  Defines the core product metrics and rules (activation, retention, NSM).  
- **Tracking plan = how we capture it**  
  Maps those definitions to concrete events, properties, and governance.

This ensures that **product decisions drive instrumentation**, not the other way around.

## Contents
- `business-logic.md` — canonical definitions of funnels, North Star metric, and key metrics.

## Repo Flow
![Escaly Repo Flow](../tracking-plan-escaly/diagrams/repo_flow.png)

This diagram shows how **business logic** informs governance,  
which shapes the tracking plan, which powers the case studies.
