import logging
import csv
from pathlib import Path

try:
    from csv_intersection.parse_args import app_arg
except ImportError:
    from parse_args import app_arg

logger: logging


def csv_compare(input1_data: dict, input2_data: dict) -> list[str]:
    # calculate common keys of data
    input1_data_keys = set(input1_data.keys())
    input2_data_keys = set(input2_data.keys())
    intersection_21 = input2_data_keys.intersection(input1_data_keys)
    # print(intersection_21)
    return list(intersection_21)


def get_csv_data(
    input_file: Path, key_index: int = 0, delimiter=",", encoding="UTF-8"
) -> tuple[list[str], dict[str, list[str]]]:
    input_data: dict[str, list[str]] = {}
    input_header: list[str] = []
    if input_file.is_file():
        with open(input_file, newline="", encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            input_header = next(reader)
            key: str = ""
            try:
                for row in reader:
                    key = Path(row[key_index]).stem
                    input_data[key] = row
            except IndexError:
                logger.error(f"{input_file} key index error: {key_index}")
    else:
        logger.error(f"File {input_file} is not found")
    return input_header, input_data


def save_result_csv(
    input_header: list[str],
    input_data: dict,
    keys: list[str],
    output: Path,
    delimiter=",",
    encoding="UTF-8",
):
    with open(output, "w", newline="", encoding=encoding) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerow(input_header)
        for key in keys:
            writer.writerow(input_data[key])
    logger.info(f"save_result_csv to {output}")


def csv_operation(input1: Path, input2: Path, output: Path):
    input1_header: list[str]
    input1_data: dict[str, list[str]]
    input2_header: list[str]
    input2_data: dict[str, list[str]]
    input1_header, input1_data = get_csv_data(input1, key_index=0)
    input2_header, input2_data = get_csv_data(input2, key_index=1)

    # print(input1_header, input1_data)
    # print(input2_header, input2_data)

    intersection_21 = csv_compare(input1_data, input2_data)
    # print(intersection_21)

    input1_records = len(input1_data.keys())
    input2_records = len(input2_data.keys())
    output_records = len(intersection_21)
    report_txt = f"{input1_records=}, {input2_records=}, {output_records=}"
    logger.info(report_txt)

    save_result_csv(input1_header, input1_data, intersection_21, output)


def main():
    global logger
    args = app_arg()
    logging.basicConfig(
        level=logging.DEBUG if args.get("verbose") else logging.INFO,
        format="%(asctime)s  %(message)s",
    )
    logger = logging.getLogger(__name__)
    work_path = args.get("work")
    input1_path = args.get("input1")
    input2_path = args.get("input2")
    output_path = args.get("output")
    if not input1_path.is_absolute():
        input1_path = work_path.joinpath(input1_path)
    if not input2_path.is_absolute():
        input2_path = work_path.joinpath(input2_path)
    if not output_path.is_absolute():
        output_path = work_path.joinpath(output_path)

    csv_operation(input1_path, input2_path, output_path)


if __name__ == "__main__":
    main()
