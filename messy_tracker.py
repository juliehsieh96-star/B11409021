import os
import json

FILENAME = "records.json"

class Tracker:
    def __init__(self):
        self.data_list = []
        self.load()

    def p_proc(self, s):
        try:
            a = s.split('/')
            if len(a) < 3:
                return None
            return {"n": a[0], "p": int(a[1]), "t": a[2]}
        except (ValueError, IndexError):
            return None

    def save(self):
        try:
            with open(FILENAME, "w") as f:
                json.dump(self.data_list, f)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load(self):
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as f:
                    self.data_list = json.load(f)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading data: {e}")

    def add_entry(self, raw_data):
        res = self.p_proc(raw_data)
        if res is not None:
            self.data_list.append(res)
            print("Added.")
        else:
            print("Error in input format.")

    def show_entries(self):
        print(json.dumps(self.data_list, indent=4))

    def calculate_totals(self):
        total = sum(item['p'] for item in self.data_list)
        cate_dict = {}
        for d in self.data_list:
            cate_dict[d['t']] = cate_dict.get(d['t'], 0) + d['p']
        return total, cate_dict

def main():
    tracker = Tracker()
    print("Welcome to System v0.1 Build 2026")
    
    while True:
        cmd = input("> ")
        
        if cmd == "exit":
            tracker.save()
            total, cate_dict = tracker.calculate_totals()
            print("Total Spend: " + str(total))
            print("Categories: " + str(cate_dict))
            break
            
        elif cmd.startswith("add "):
            raw_data = cmd[4:]
            tracker.add_entry(raw_data)
        
        elif cmd == "show":
            tracker.show_entries()
            
        elif cmd == "clear_all_danger":
            tracker.data_list.clear()
            if os.path.exists(FILENAME):
                os.remove(FILENAME)

if __name__ == "__main__":
    main()
