import pandas as pd
import re


def main():
    df = pd.read_csv("sample.txt", header=None, names=["full_text"], sep="<>")
    df["flow_rate"] = df["full_text"].apply(lambda x: re.search(r"-?\d+", x).group())
    df["beacon"] = df["beacon"].apply(lambda x: list(map(int, re.findall(r"-?\d+", x))))

if __name__ == "__main__":
    main()
