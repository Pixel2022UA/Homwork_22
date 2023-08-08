import re


def test_find_emails():
    text = "My mail are test@example.com and another@example.org"
    my_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(my_pattern, text)
    assert len(emails) == 2
    assert "test@example.com" in emails
    assert "another@example.org" in emails


def test_validate_date():
    valid_dates = ["01/31/2023", "12/15/2022", "06/05/2021"]
    invalid_dates = ["31/01/2023", "15-12-2022", "2021/06/05"]
    my_pattern = r"\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}\b"
    for date in valid_dates:
        assert re.match(my_pattern, date) is not None
    for date in invalid_dates:
        assert re.match(my_pattern, date) is None


def test_extract_name_and_domain():
    email = "test@example.com"
    my_pattern = r"(\b[A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\b"
    data = re.match(my_pattern, email)
    assert data is not None
    assert data.group(1) == "test"
    assert data.group(2) == "example.com"


def test_validate_phone_number():
    valid_numbers = ["1234567890", "5555555555", "9876543210"]
    invalid_numbers = ["1234-567-890", "555-555-555", "9876543210x"]
    my_pattern = r"^\d{10}$"
    for number in valid_numbers:
        assert re.match(my_pattern, number) is not None
    for number in invalid_numbers:
        assert re.match(my_pattern, number) is None


def test_split_text_into_sentences():
    text = "A am not a student yet! I have completed courses Pyton Pro."
    my_pattern = r"[.!]"
    sentences = re.split(my_pattern, text)

    assert len(sentences) == 3
    assert sentences[0] == "A am not a student yet"
    assert sentences[1] == " I have completed courses Pyton Pro"
    assert sentences[2] == ""
