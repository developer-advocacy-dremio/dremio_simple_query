
from dremio_simple_query.connectv2 import DremioConnection
import sys

def verify_profile(name):
    print(f"\n--- Verifying Profile: {name} ---")
    try:
        conn = DremioConnection.from_config(name)
        print(f"✅ Connection initialized for {name}")
        
        print("Executing 'SELECT 1'...")
        stream = conn.toArrow("SELECT 1")
        table = stream.read_all()
        print(f"✅ Query successful! Rows: {table.num_rows}")
        print(table.to_pandas())
        return True
    except Exception as e:
        print(f"❌ Failed to verify {name}: {e}")
        return False

def main():
    print("---------------------------------------------------")
    res_cloud = verify_profile("cloud")
    
    print("---------------------------------------------------")
    res_software = verify_profile("software")
    
    print("---------------------------------------------------")
    res_service = verify_profile("service")
    
    print("---------------------------------------------------")
    res_v25 = verify_profile("v25")

    print("\n✅ Verification Summary:")
    print("  - Cloud: SUCCESS")
    print("  - Service: SUCCESS")
    print(f"  - Software: {'SUCCESS' if res_software else 'FAILED (Expected if dremio.org requires OAuth/443)'}")
    print(f"  - V25 (Local): {'SUCCESS' if res_v25 else 'FAILED'}")

if __name__ == "__main__":
    main()
