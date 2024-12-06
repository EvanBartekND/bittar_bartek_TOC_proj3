#!/usr/bin/env python3
import csv

class KTapeTM:
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            reader = csv.reader(f)
            lines = [line for line in reader]
        
        first_line = lines[0][0].split(",")
        self.name = first_line[0].strip()
        self.k = int(first_line[0].strip())
        
        self.state_names = lines[1][0].split(",")
        self.alphabet = lines[2][0].split(",")
        self.blank_symbol = lines[3][0]
        
        self.transitions = []
        for line in lines[4:]:
            if len(line) > 0:
                self.transitions.append(line[0].split(","))
        
        self.tapes = []
        self.heads = []
        self.current_state = None
        self.final_states = set()

    def initialize(self, input_string):
        self.tapes = [[" "] * 1000 for _ in range(self.k)]
        self.heads = [500] * self.k
        
        for i, c in enumerate(input_string):
            self.tapes[0][500 + i] = c
        self.current_state = "q0"

    def step(self):
        head_symbols = [self.tapes[i][self.heads[i]] for i in range(self.k)]
        for t in self.transitions:
            state = t[0]
            conditions = t[1:self.k + 1]
            new_state = t[self.k + 1]
            actions = t[self.k + 2:]

            if state != self.current_state:
                continue
            if all(c == "*" or c == s for c, s in zip(conditions, head_symbols)):
                self.current_state = new_state
                for i in range(self.k):
                    if actions[i] != "*":
                        self.tapes[i][self.heads[i]] = actions[i]
                    if actions[self.k + i] == "L":
                        self.heads[i] -= 1
                    elif actions[self.k + i] == "R":
                        self.heads[i] += 1
                return True
        return False

    def run(self, input_string):
        self.initialize(input_string)
        step_count = 0
        print(f"{self.name} {input_string}")
        
        while self.current_state not in self.final_states:
            print(f"Step {step_count}:")
            for tape in self.tapes:
                print("".join(tape[:self.heads[0]]) + " " + tape[self.heads[0]] + "".join(tape[self.heads[0] + 1:]))
            
            if not self.step():
                print("Machine halted unexpectedly.")
                return
            step_count += 1
        
        print("Accepted.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./ktape_KeoughKitch.py <csv_file> <input_string>")
    else:
        tm = KTapeTM(sys.argv[1])
        tm.run(sys.argv[2])

