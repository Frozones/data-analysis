import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample.csv")

print("Average read speed:", df["read_speed"].mean())
print("Average write speed:", df["write_speed"].mean())

failed = df[df["status"] == "FAIL"]
print("\nFailed units:")
print(failed)

plt.hist(df["read_speed"], bins=5, edgecolor='black')
plt.title("Read Speed Distribution")
plt.xlabel("Read Speed (MB/s)")
plt.ylabel("Count")
plt.show()
