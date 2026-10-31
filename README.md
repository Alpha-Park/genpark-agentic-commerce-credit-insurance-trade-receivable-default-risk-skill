# genpark-agentic-commerce-credit-insurance-trade-receivable-default-risk-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

B2B trade credit insurance debtor limit utilization, Altman Z-Score commercial bankruptcy sentinel.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `evaluate_trade_credit_insurance_risk`
- **Category**: `agentic_commerce`

### Method Documentation
Evaluate B2B trade credit insurance portfolio risk (Allianz Trade / Atradius / Coface).
Computes credit policy limit utilization, Days Sales Outstanding (DSO) aging, debtor Altman Z-Score commercial default risk,
and insured indemnity claim payouts (e.g. 90% indemnification ratio).

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "evaluate_trade_credit_insurance_risk",
    "arguments": {
    "insured_credit_limit_usd": 250000.0,
    "current_open_ar_usd": 210000.0,
    "overdue_ar_usd": 48000.0,
    "altman_z_score": 1.72,
    "indemnification_ratio_pct": 90.0
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
