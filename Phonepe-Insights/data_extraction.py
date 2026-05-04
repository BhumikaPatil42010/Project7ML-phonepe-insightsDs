# import os
# import json
# import pandas as pd

# # Path to aggregated transaction data
# path = "D:/phonepe-insights/data/raw/pulse/data/aggregated/transaction/country/india/state/"


# data = []

# for state in os.listdir(path):
#     state_path = os.path.join(path, state)
    
#     for year in os.listdir(state_path):
#         year_path = os.path.join(state_path, year)
        
#         for file in os.listdir(year_path):
#             file_path = os.path.join(year_path, file)
            
#             with open(file_path, 'r') as f:
#                 content = json.load(f)
                
#                 try:
#                     for item in content["data"]["transactionData"]:
#                         data.append({
#                             "state": state,
#                             "year": int(year),
#                             "quarter": int(file.strip(".json")),
#                             "type": item["name"],
#                             "count": item["paymentInstruments"][0]["count"],
#                             "amount": item["paymentInstruments"][0]["amount"]
#                         })
#                 except:
#                     pass

# df = pd.DataFrame(data)

# # Save CSV
# output_path = "data/processed/aggregated_transaction.csv"
# df.to_csv(output_path, index=False)

# print("✅ Aggregated Transaction Data Extracted!")









import os
import json
import pandas as pd
import os

base = "data/raw/pulse/data/map/transaction/"

for root, dirs, files in os.walk(base):
    print(root)
    break

# Base path
BASE_PATH = "D:/phonepe-insights/data/raw/pulse/data/"


# Ensure output folder exists
os.makedirs("data/processed", exist_ok=True)

# ------------------------------------------
# 1. Aggregated Transaction
# ------------------------------------------
def aggregated_transaction():
    path = BASE_PATH + "aggregated/transaction/country/india/state/"
    data = []

    for state in os.listdir(path):
        for year in os.listdir(path + state):
            for file in os.listdir(path + state + "/" + year):
                with open(path + state + "/" + year + "/" + file) as f:
                    d = json.load(f)
                    try:
                        for item in d["data"]["transactionData"]:
                            data.append([
                                state,
                                int(year),
                                int(file.strip(".json")),
                                item["name"],
                                item["paymentInstruments"][0]["count"],
                                item["paymentInstruments"][0]["amount"]
                            ])
                    except:
                        pass

    df = pd.DataFrame(data, columns=["state","year","quarter","type","count","amount"])
    df.to_csv("data/processed/aggregated_transaction.csv", index=False)
    print("aggregated_transaction done")


# ------------------------------------------
# 2. Aggregated User
# ------------------------------------------
def aggregated_user():
    path = BASE_PATH + "aggregated/user/country/india/state/"
    data = []

    for state in os.listdir(path):
        for year in os.listdir(path + state):
            for file in os.listdir(path + state + "/" + year):
                with open(path + state + "/" + year + "/" + file) as f:
                    d = json.load(f)
                    try:
                        data.append([
                            state,
                            int(year),
                            int(file.strip(".json")),
                            d["data"]["aggregated"]["registeredUsers"],
                            d["data"]["aggregated"]["appOpens"]
                        ])
                    except:
                        pass

    df = pd.DataFrame(data, columns=["state","year","quarter","registeredUsers","appOpens"])
    df.to_csv("data/processed/aggregated_user.csv", index=False)
    print("aggregated_user done")


# ------------------------------------------
# 3. Map Transaction
# ------------------------------------------
# def map_transaction():
#     import os
#     import json
#     import pandas as pd
   

#     base_path = BASE_PATH + "map/transaction/"
#     data = []

#     # Walk through ALL subfolders automatically
#     for root, dirs, files in os.walk(base_path):
#         for file in files:
#             if file.endswith(".json"):
#                 file_path = os.path.join(root, file)
                
#                 with open(file_path) as f:
#                     d = json.load(f)
#                     print(d)
#                     break

#                     try:
#                         # Extract state, year from path
#                         parts = root.split(os.sep)

#                         state = parts[-2]   # adjust if needed
#                         year = parts[-1]

#                         for item in d["data"]["hoverDataList"]:
#                             data.append([
#                                 state,
#                                 int(year),
#                                 int(file.strip(".json")),
#                                 item["name"],
#                                 item["metric"][0]["count"],
#                                 item["metric"][0]["amount"]
#                             ])
#                     except:
#                         pass

#     df = pd.DataFrame(data, columns=["state","year","quarter","district","count","amount"])
#     df.to_csv("data/processed/map_transaction.csv", index=False)

#     print("map_transaction done")



def map_transaction():
    import os, json, pandas as pd

    base_path = BASE_PATH + "map/transaction/"
    data = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)

                with open(file_path) as f:
                    d = json.load(f)

                    try:
                        for item in d["data"]["hoverDataList"]:
                            data.append([
                                root.split(os.sep)[-2],   # state
                                root.split(os.sep)[-1],   # year
                                int(file.strip(".json")),
                                item["name"],
                                item["metric"][0]["count"],
                                item["metric"][0]["amount"]
                            ])
                    except:
                        pass

    df = pd.DataFrame(data, columns=["state","year","quarter","district","count","amount"])
    df.to_csv("data/processed/map_transaction.csv", index=False)

    print("map_transaction done")


# ------------------------------------------
# 4. Top Transaction (District)
# ------------------------------------------
def top_transaction():
    path = BASE_PATH + "top/transaction/country/india/state/"
    data = []

    for state in os.listdir(path):
        for year in os.listdir(path + state):
            for file in os.listdir(path + state + "/" + year):
                with open(path + state + "/" + year + "/" + file) as f:
                    d = json.load(f)
                    try:
                        for item in d["data"]["districts"]:
                            data.append([
                                state,
                                int(year),
                                int(file.strip(".json")),
                                item["entityName"],
                                item["metric"]["count"],
                                item["metric"]["amount"]
                            ])
                    except:
                        pass

    df = pd.DataFrame(data, columns=["state","year","quarter","district","count","amount"])
    df.to_csv("data/processed/top_transaction.csv", index=False)
    print("top_transaction done")


# ------------------------------------------
# RUN ALL
# ------------------------------------------
if __name__ == "__main__":
    aggregated_transaction()
    aggregated_user()
    map_transaction()
    top_transaction()

    print("\n ALL DATA EXTRACTED SUCCESSFULLY!")