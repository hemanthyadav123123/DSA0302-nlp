print("DFA Simulator")

states = input("Enter states (comma separated): ").split(",")
alphabet = input("Enter input alphabet (comma separated): ").split(",")

states = [s.strip() for s in states]
alphabet = [a.strip() for a in alphabet]

transition = {}

print("\nEnter transition table:")

for state in states:
    transition[state] = {}
    for symbol in alphabet:
        transition[state][symbol] = input("Transition(" + state + "," + symbol + ") = ").strip()

initial_state = input("\nEnter initial state: ").strip()

final_states = input("Enter final state(s) (comma separated): ").split(",")
final_states = [s.strip() for s in final_states]

n = int(input("\nEnter number of input strings: "))

for i in range(n):
    string = input("\nEnter input string " + str(i + 1) + ": ").strip()

    current_state = initial_state
    path = current_state
    valid = True

    for symbol in string:
        if symbol not in alphabet:
            valid = False
            break
        current_state = transition[current_state][symbol]
        path += " -> " + current_state

    print("Transition Path:")
    print(path)

    if valid and current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
