import os
import json

RECORDS_FILENAME = "records.json"


class ExpenseTracker:
    def __init__(self, filename=RECORDS_FILENAME):
        self.filename = filename
        self.records = []
        self.load()

    def parse_entry(self, raw_entry):
        if not raw_entry:
            raise ValueError("Input cannot be empty.")

        parts = raw_entry.split("/")
        if len(parts) != 3:
            raise ValueError("Input must be in the format: name/amount/category")

        name, amount_text, category = [part.strip() for part in parts]
        if not name or not amount_text or not category:
            raise ValueError("Name, amount, and category cannot be empty.")

        try:
            amount = int(amount_text)
        except ValueError:
            raise ValueError("Amount must be an integer.")

        return {"name": name, "amount": amount, "category": category}

    def add_entry(self, raw_entry):
        record = self.parse_entry(raw_entry)
        self.records.append(record)
        print("Added.")

    def normalize_record(self, record):
        if not isinstance(record, dict):
            return None

        if "name" in record and "amount" in record and "category" in record:
            return {
                "name": str(record["name"]),
                "amount": int(record["amount"]),
                "category": str(record["category"]),
            }

        if "n" in record and "p" in record and "t" in record:
            try:
                return {
                    "name": str(record["n"]),
                    "amount": int(record["p"]),
                    "category": str(record["t"]),
                }
            except (ValueError, TypeError):
                return None

        return None

    def load(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                loaded_records = json.load(f)
                if not isinstance(loaded_records, list):
                    raise ValueError("Data file must contain a list of records.")

                self.records = []
                for record in loaded_records:
                    normalized = self.normalize_record(record)
                    if normalized is not None:
                        self.records.append(normalized)
        except (IOError, json.JSONDecodeError, ValueError) as error:
            print(f"Error loading data: {error}")
            self.records = []

    def save(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.records, f, indent=4, ensure_ascii=False)
        except IOError as error:
            print(f"Error saving data: {error}")

    def display_records(self):
        print(json.dumps(self.records, indent=4, ensure_ascii=False))

    def calculate_totals(self):
        total_amount = sum(record["amount"] for record in self.records)
        category_totals = {}
        for record in self.records:
            category_totals[record["category"]] = category_totals.get(record["category"], 0) + record["amount"]
        return total_amount, category_totals


def main():
    tracker = ExpenseTracker()
    print("Welcome to ExpenseTracker v0.1")
    print("Commands: add <name>/<amount>/<category>, show, save, exit")

    while True:
        command = input("> ").strip()
        if not command:
            continue

        if command == "exit":
            tracker.save()
            total_amount, category_totals = tracker.calculate_totals()
            print(f"Total Spend: {total_amount}")
            print(f"Category Totals: {category_totals}")
            break

        if command == "show":
            tracker.display_records()
            continue

        if command == "save":
            tracker.save()
            print("Saved.")
            continue

        if command.startswith("add "):
            raw_entry = command[4:].strip()
            try:
                tracker.add_entry(raw_entry)
            except ValueError as error:
                print(f"Error: {error}")
            continue

        print("Unknown command. Use add, show, save, or exit.")


if __name__ == "__main__":
    main()
