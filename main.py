from rotator import word_rotator_core as rotate, WRCoreException
from pathlib import Path


INPUT_PATH = Path("input_files/input_file.txt")
OUTPUT_PATH = Path("output_files/output_file.txt")


def rotate_file(in_path: Path, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    results: list[str] = []
    with in_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")          # odstraním jen konec řádku
            results.append(rotate(line) + "\n")

    with out_path.open("w", encoding="utf-8") as f:
        f.writelines(results)


def main() -> None:
    while True:
        text = input("Write your word or a sentence: ")
        print(rotate(text))

        cmd = input(
            "To stop write 'stop', to rotate from file write 'file', to continue press Enter: "
        ).strip().lower()

        if cmd == "stop":
            print("The game is over :)")
            return
        elif cmd == "file":
            rotate_file(INPUT_PATH, OUTPUT_PATH)
            print("The output_file.txt has been created.")


if __name__ == "__main__":
    try:
        main()
    except WRCoreException as err:
        print(err)
    except FileNotFoundError as err:
        print(f"File error: {err}")
