import csv

class TuringMachine:
    def __init__(self, tm_file):
        self.name = ""
        self.states = []
        self.input_alphabet = []
        self.tape_alphabet = []
        self.start_state = ""
        self.accept_state = ""
        self.reject_state = ""
        self.transitions = {}
        self._load_tm(tm_file)

    def _load_tm(self, tm_file):
        with open(tm_file, 'r') as file:
            reader = csv.reader(file)
            self.name = next(reader)[0]
            self.states = next(reader)
            self.input_alphabet = next(reader)
            self.tape_alphabet = next(reader)
            self.start_state = next(reader)[0]
            self.accept_state = next(reader)[0]
            self.reject_state = next(reader)[0]

            for row in reader:
                state, symbol, next_state, write_symbol, direction = row
                if (state, symbol) not in self.transitions:
                    self.transitions[(state, symbol)] = []
                self.transitions[(state, symbol)].append((next_state, write_symbol, direction))

    def get_next_configurations(self, state, tape, head_pos):
        current_symbol = tape[head_pos] if head_pos < len(tape) else "_"
        next_steps = self.transitions.get((state, current_symbol), [])
        next_configurations = []

        for next_state, write_symbol, direction in next_steps:
            new_tape = list(tape)
            if head_pos < len(new_tape):
                new_tape[head_pos] = write_symbol
            else:
                new_tape.append(write_symbol)

            new_head_pos = head_pos + (1 if direction == 'R' else -1)
            if new_head_pos < 0:
                new_tape.insert(0, "_")
                new_head_pos = 0

            next_configurations.append((next_state, new_tape, new_head_pos))

        return next_configurations

def trace_ntm(tm_file, input_string, max_depth=100, max_steps=1000):
    
    tm = TuringMachine(tm_file)
    # print(f"Turing Machine: {tm.name}")
    # print(f"Input String: {input_string}")
    # Initial tape setup
    initial_tape = list(input_string)
    initial_configuration = (tm.start_state, initial_tape, 0)
    configuration_tree = [[initial_configuration]]

    total_transitions = 0
    total_configurations = 0
    total_children = 0

    for depth in range(max_depth):
        current_level = configuration_tree[-1]
        next_level = []
        total_configurations += len(current_level)

        for state, tape, head_pos in current_level:
            if state == tm.accept_state:
                print("\n--- Summary ---")

                print(f"String accepted in {depth} transitions.")
                # print_trace(configuration_tree)
                print_summary(tm, input_string, depth, total_transitions, total_configurations, total_children)
                return
            elif state != tm.reject_state:
                children = tm.get_next_configurations(state, tape, head_pos)
                next_level.extend(children)
                total_children += len(children)

            total_transitions += 1
            if total_transitions >= max_steps:
                print("\n--- Summary ---")
                print(f"Execution stopped after {max_steps} steps.")
                print_summary(tm, input_string, depth, total_transitions, total_configurations, total_children)
                return

        if not next_level:
            print(f"String rejected in {depth} transitions.")
            print_summary(tm, input_string, depth, total_transitions, total_configurations, total_children)
            return

        configuration_tree.append(next_level)

    print(f"Execution stopped after reaching max depth of {max_depth}.")
    print_summary(tm, input_string, max_depth, total_transitions, total_configurations, total_children)

# used to debug
def print_trace(configuration_tree):
    print("Path to accept:")
    for depth, configurations in enumerate(configuration_tree):
        print(f"Depth {depth}:")
        for state, tape, head_pos in configurations:
            left_of_head = ''.join(tape[:head_pos])
            head_char = tape[head_pos] if head_pos < len(tape) else "_"
            right_of_head = ''.join(tape[head_pos + 1:])
            print(f"{left_of_head}, {state}, {head_char}, {right_of_head}")
# Function to print summary of simulation
def print_summary(tm, input_string, depth, transitions, total_configurations, total_children):
    avg_nondeterminism = total_children / total_configurations if total_configurations > 0 else 0
    print(f"Machine Name: {tm.name}")
    print(f"Input String: {input_string}")
    print(f"Depth of Configurations: {depth}")
    print(f"Total Transitions Simulated: {transitions}")
    print(f"Average Non-determinism: {avg_nondeterminism:.2f}")
    print("----------------\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Trace NTM behavior.")
    parser.add_argument("tm_file", help="Path to the Turing Machine .csv file")
    parser.add_argument("input_string", help="Input string for the Turing Machine")
    parser.add_argument("--max_depth", type=int, default=100, help="Maximum depth of exploration")
    parser.add_argument("--max_steps", type=int, default=1000, help="Maximum number of steps to simulate")

    args = parser.parse_args()

    trace_ntm(args.tm_file, args.input_string, args.max_depth, args.max_steps)
