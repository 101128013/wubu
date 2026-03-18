"""Main entry point"""
import sys
from osint_master_orchestrator import OSINTMasterOrchestrator

if __name__ == "__main__":
    email = sys.argv[1] if len(sys.argv) > 1 else "nickfoy.design@gmail.com"
    orchestrator = OSINTMasterOrchestrator(email)
    orchestrator.run_all_levels()