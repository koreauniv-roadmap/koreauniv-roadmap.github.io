import json
import os

input_dir = "input_json"
output_dir = "output_json"

os.makedirs(output_dir, exist_ok=True)

# 학수번호 변경 규칙
code_map = {
    "GECT002": "UNIV020",
    "GEBT001": "UNIV040",
    "GECT003": "UNIV021"
}

remove_words = ["[진로 창업]", "[진로창업]"]

def modify_course(course):
    # 학수번호 변경
    code = course.get("학수번호")
    if code in code_map:
        course["학수번호"] = code_map[code]

    # 교과목명 수정
    name = course.get("교과목명", "")
    for w in remove_words:
        name = name.replace(w, "")
    course["교과목명"] = name.strip()

    return course


def modify_files(directory, save_directory):

    os.makedirs(save_directory, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            try:
                with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                    courses = json.load(file)

                # 모든 과목 수정
                courses = [modify_course(c) for c in courses]

                output_file = os.path.join(
                    save_directory,
                    f"{os.path.splitext(filename)[0]}.json"
                )

                with open(output_file, "w", encoding="utf-8") as outfile:
                    json.dump(courses, outfile, ensure_ascii=False, indent=4)

                print(f"✔ processed: {filename}")
                print(f"Processed {filename} -> {output_file}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    directory = "./course_files"
    save_directory = "./course_files2"
    modify_files(directory, save_directory)
    
