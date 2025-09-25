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
