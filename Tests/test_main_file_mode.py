from pathlib import Path
from main import rotate_file  # předpoklad: v main.py máš rotate_file()


def test_rotate_file_creates_output(tmp_path: Path):
    # Arrange
    input_dir = tmp_path / "input_files"
    output_dir = tmp_path / "output_files"
    input_dir.mkdir()
    output_dir.mkdir()

    in_file = input_dir / "input_file.txt"
    out_file = output_dir / "output_file.txt"

    in_file.write_text("Nexi, Ty mi dáváš kapky!\nAGI\n", encoding="utf-8")

    # Act
    rotate_file(in_file, out_file)

    # Assert
    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")

    # edukativně: ověř konkrétní transformaci po řádcích
    lines = content.splitlines()
    assert lines[0] == "Ixen, Yt im šávád ykpak!"
    assert lines[1] == "IGA"
