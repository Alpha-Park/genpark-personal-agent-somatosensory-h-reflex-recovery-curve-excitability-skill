"""
MCP Server for Somatosensory H-Reflex Recovery Curve Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import HReflexRecoveryCurveClient


def main():
    client = HReflexRecoveryCurveClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_recovery_curve",
                            "description": "Calculates Hoffmann Reflex (H-reflex) paired-pulse recovery ratios (H2/H1%), Early Depression Index, and Central Spinal Disinhibition Index across inter-stimulus intervals.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "h1_baseline_amplitude_mv": {
                                        "type": "number",
                                        "description": "Unconditioned baseline H-reflex amplitude in mV."
                                    },
                                    "isi_responses": {
                                        "type": "array",
                                        "description": "List of responses at variable ISIs, each having 'isi_ms' and 'h2_amplitude_mv'.",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "isi_ms": {"type": "number"},
                                                "h2_amplitude_mv": {"type": "number"}
                                            },
                                            "required": ["isi_ms", "h2_amplitude_mv"]
                                        }
                                    },
                                    "m_max_amplitude_mv": {
                                        "type": "number",
                                        "description": "Maximal direct muscle motor response M_max in mV (optional)."
                                    }
                                },
                                "required": [
                                    "h1_baseline_amplitude_mv",
                                    "isi_responses"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_recovery_curve":
                try:
                    out = client.evaluate_recovery_curve(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
