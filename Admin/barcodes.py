import barcode
from barcode.writer import ImageWriter
from time import sleep


def make_barcode(code12, output_name):
    if not code12.isdigit() or len(code12) != 12:
        raise ValueError("Code must be exactly 12 digits.")

    # Use Code 128 so the value is encoded EXACTLY as given
    code128 = barcode.get("code128", code12, writer=ImageWriter())

    options = {
        "module_width": 0.4,
        "module_height": 15.0,
        "font_size": 14,
        "text_distance": 5.0,
        "quiet_zone": 6.5,
        "write_text": True,
    }

    filename = code128.save(output_name, options=options)
    print("Saved:", filename)


if __name__ == "__main__":
    codes = [
        "013520260001",
        "013520260002",
        "013520260003",
        "013520260004",
        "013520260005",
        "013520260006",
        "013520260007",
        "013520260008",
        "013520260009",
        "013520260010",
        "013520260011",
        "013520260012"
    ]

    for c in codes:
        sleep(0.1)
        make_barcode(c, "student_barcode_" + c)