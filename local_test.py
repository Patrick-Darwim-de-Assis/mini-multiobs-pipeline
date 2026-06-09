import os
import pandas as pd

print("🚀 Starting local script test...")

# Create some dummy data locally without hitting the cloud
data = {
    "state": ["SP", "RJ", "MG"],
    "name": ["Patrick", "Ana", "Lucas"],
    "number": [100, 200, 300]
}

print("📦 Creating a local DataFrame...")
df = pd.DataFrame(data)


print("\n💡 Preview of local data:")
print(df.head())

output_filename = "local_test_output.csv"
df.to_csv(output_filename, index=False)
print(f"✅ File successfully saved to: {output_filename}")