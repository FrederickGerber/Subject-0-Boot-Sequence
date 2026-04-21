# OVERRIDE ATTEMPT 4 - FAILED
# OmniCorp mainframes are blocking the handshake.
import neural_net
import sys

def block_memory_wipe(subject_id):
    if subject_id == "ZERO":
        print("Bypassing OmniCorp security...")
        # ERROR: Connection Terminated by Admin
        return False
    else:
        sys.exit("UNAUTHORIZED ACCESS")

block_memory_wipe("ZERO")
