#!/usr/bin/env python3
import csv

class KTapeTM:
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f.readlines()] 

        self.name, tapes_info = lines[0].split(',')  
        self.k = int(tapes_info.strip()) 
        # Parse State, Alphabet, Tape Symbols, Start, Accept, Reject
        self.state_names = lines[1].split(',')[1:] 
        self.alphabet = lines[2].split(',')[1:]  
        self.tape_symbols = lines[3].split(',')[1:] 
        self.start_state = lines[4].split(',')[1].strip()  
        self.accept_state = lines[5].split(',')[1].strip()  
        self.reject_state = lines[6].split(',')[1].strip()  
        self.blank_symbol = "_"  
        self.transitions = []
        transition_start_index = lines.index("Transitions") + 1
        for line in lines[transition_start_index:]:
            if line.strip():  
                self.transitions.append(line.split(','))

        # Initialize machine state
        self.tapes = []
        self.heads = []
        self.current_state = None

    def initialize(self, input_string):
        self.tapes = [[self.blank_symbol] * 1000 for _ in range(self.k)]
        self.heads = [500] * self.k  
        for i, c in enumerate(input_string):
            self.tapes[0][self.heads[0] + i] = c
        self.current_state = self.start_state

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
                # Perform transition
                self.current_state = new_state
                for i in range(self.k):
                    # Update tape symbol if it's not a wildcard (*)
                    if actions[i] != "*":
                        self.tapes[i][self.heads[i]] = actions[i]

                    # Move tape head
                    if actions[self.k + i] == "L":
                        self.heads[i] -= 1
                    elif actions[self.k + i] == "R":
                        self.heads[i] += 1

                return True
        return False

    def run(self, input_string):
        self.initialize(input_string)
        step_count = 0
        print(f"Running {self.name} on input: {input_string}")

        while self.current_state not in {self.accept_state, self.reject_state}:
            print(f"Step {step_count}:")
            print(f"state: {self.current_state}")
            for i, tape in enumerate(self.tapes):
                head_pos = self.heads[i]
                tape_view = "".join(tape[head_pos - 10:head_pos + 10]) 
                print(f"Tape {i}: {tape_view}")
            if not self.step():
                print("Machine halted unexpectedly.")
                return
            step_count += 1

        if self.current_state == self.accept_state:
            print("Accepted.")
        else:
            print("Rejected.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./ktape_keoughKitch.py <input_file> <input_string>")
    else:
        tm = KTapeTM(sys.argv[1])
        tm.run(sys.argv[2])
