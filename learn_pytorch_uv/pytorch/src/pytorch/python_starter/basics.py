"""Python 基础：函数、类型提示、数据类、文件和 JSON。"""

from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass
class Student:
    name: str
    age: int
    skills: list[str]


def calculate_average(scores: list[float]) -> float:
    """计算平均分；空列表时返回 0。"""
    return sum(scores) / len(scores) if scores else 0.0


def save_student(student: Student, output_dir: Path) -> Path:
    """把对象转换成 JSON，保存到项目的 data 目录。"""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "student.json"
    output_file.write_text(
        json.dumps(asdict(student), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_file


def main() -> None:
    student = Student("小明", 20, ["Python", "Git", "SQL"])
    scores = [88.5, 92, 79.5]
    print(f"{student.name} 的平均分：{calculate_average(scores):.2f}")
    print(f"JSON 文件：{save_student(student, Path('data'))}")


if __name__ == "__main__":
    main()
