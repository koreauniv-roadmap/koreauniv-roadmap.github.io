import json
import csv

input_directory = "./course_files"
output_directory = "./course_csv"
    
# 파일 경로
json_file = f"{input_directory}/환경생태공학부.json"
csv_file = f"{output_directory}/환경생태공학부.csv"

# JSON 읽기
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# JSON이 dict 하나일 경우 대비
if isinstance(data, dict):
    data = [data]

# CSV 저장
with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"CSV 파일 생성 완료: {csv_file}")