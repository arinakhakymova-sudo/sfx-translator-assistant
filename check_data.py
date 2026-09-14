import pandas as pd

VALID_TAGS = {"impact", "motion", "body", "voice", "object", "mood"}

df = pd.read_csv("data/sfx_pairs.csv")

# strip stray spaces from column names and from the tags themselves
df.columns = df.columns.str.strip()
df["context"] = df["context"].str.strip().str.lower()

print(f"rows: {len(df)}")
print(f"columns: {list(df.columns)}")
print()

print("rows per context tag:")
print(df["context"].value_counts())
print()

unknown = set(df["context"].dropna().unique()) - VALID_TAGS
if unknown:
    print(f"WARNING: tags that aren't in the list: {unknown}")
else:
    print("all tags valid")
print()

missing = df[df["sfx_ua"].isna() | df["sfx_en"].isna()]
if len(missing) > 0:
    print(f"WARNING: {len(missing)} rows missing en or ua")
    print(missing[["id", "sfx_en", "sfx_ua"]])
else:
    print("no missing sound effects")
