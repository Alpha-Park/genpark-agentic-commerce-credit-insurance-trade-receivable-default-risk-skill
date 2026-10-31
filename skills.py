# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-credit-insurance-trade-receivable-default-risk-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def evaluate_trade_credit_insurance_risk(insured_credit_limit_usd, current_open_ar_usd, overdue_ar_usd, altman_z_score=2.8, indemnification_ratio_pct=90.0):
    if insured_credit_limit_usd <= 0:
        raise ValueError("insured_credit_limit_usd must be greater than zero")
        
    credit_limit_utilization_pct = (current_open_ar_usd / insured_credit_limit_usd) * 100.0
    overdue_ratio_pct = (overdue_ar_usd / current_open_ar_usd * 100.0) if current_open_ar_usd > 0 else 0.0
    
    # Altman Z-Score interpretation:
    # Z > 2.99: Safe Zone
    # 1.81 <= Z <= 2.99: Grey Zone
    # Z < 1.81: Distress Zone (high bankruptcy probability within 2 years)
    if altman_z_score < 1.81:
        insolvency_risk = "DISTRESS_ZONE_HIGH_INSOLVENCY_RISK"
        policy_action = "Issue formal Notice of Overdue Account (NOA) to insurer; stop further shipments."
    elif altman_z_score <= 2.99:
        insolvency_risk = "GREY_ZONE_MODERATE_RISK"
        policy_action = "Place account on watch; negotiate bank guarantee or reduce credit term to Net 15."
    else:
        insolvency_risk = "SAFE_ZONE_LOW_RISK"
        policy_action = "Maintain standard credit terms."
        
    potential_claim_indemnity_usd = overdue_ar_usd * (indemnification_ratio_pct / 100.0)
    uninsured_credit_loss_usd = overdue_ar_usd - potential_claim_indemnity_usd
    
    return {
        "insured_credit_limit_usd": insured_credit_limit_usd,
        "current_open_ar_usd": current_open_ar_usd,
        "credit_limit_utilization_pct": round(credit_limit_utilization_pct, 1),
        "limit_exceeded": credit_limit_utilization_pct > 100.0,
        "overdue_receivables_usd": overdue_ar_usd,
        "overdue_ratio_pct": round(overdue_ratio_pct, 1),
        "altman_z_score": round(altman_z_score, 2),
        "counterparty_solvency_tier": insolvency_risk,
        "estimated_insurance_indemnity_usd": round(potential_claim_indemnity_usd, 2),
        "net_uninsured_exposure_usd": round(uninsured_credit_loss_usd, 2),
        "mandatory_credit_action": policy_action
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "evaluate_trade_credit_insurance_risk",
                        "description": """Evaluate B2B trade credit insurance portfolio risk (Allianz Trade / Atradius / Coface).
Computes credit policy limit utilization, Days Sales Outstanding (DSO) aging, debtor Altman Z-Score commercial default risk,
and insured indemnity claim payouts (e.g. 90% indemnification ratio).""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = evaluate_trade_credit_insurance_risk(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'insured_credit_limit_usd': 250000.0, 'current_open_ar_usd': 210000.0, 'overdue_ar_usd': 48000.0, 'altman_z_score': 1.72, 'indemnification_ratio_pct': 90.0}
        out = evaluate_trade_credit_insurance_risk(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
