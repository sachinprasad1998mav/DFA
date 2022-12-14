# Write code to simulate the Deterministic Finite Automata DFA M = (Q, q0, A, sigma, delta) on string w.
# In particular, your implementation should include a functionturning the sequenceof states visitedby dfa for w.

class DFA:

    # Constructor of the class DFA, accepting the required values to build DFA.
    def __init__(self):
        self.Q = self.populate_states()
        self.startState = self.set_start()
        self.acceptState = self.set_accept()
        self.SIGMA = self.populate_alphabet()
        self.DELTA = self.populate_transition_function()
        self.CURRENT_STATE = None

    # Function to set the start state.
    def set_start(self):
        start = input("Enter the START_STATE: ")
        return start

    # Function to set the accept states.
    def set_accept(self):
        while (True):
            accept = input("Enter the ACCEPT_STATES: ").split()
            return accept

    # Function accepting states of the DFA.
    def populate_states(self):
        Q_input = input("Enter list of states separated by spaces: ").split()
        print("STATES : {}".format(Q_input))
        return Q_input

    # Function accepting alphabets of the DFA.
    def populate_alphabet(self):
        SIGMA_input = input(
            "Enter input alphabet separated by spaces: ").split()
        print("ALPHABET : {}".format(SIGMA_input))
        return SIGMA_input

    # Function creating a transition table, and printing it.
    # We particularly use dictonary, to map states of the DFA.
    # eg,
    #     dfa =
    #         {
    #             q0 : { 0:q0 , 1:q1},
    #             q1 : { 0:q1 , 1:q0 }
    #         }
    def populate_transition_function(self):
        transition_dict = {
            el: {el_2: '' for el_2 in self.SIGMA} for el in self.Q}

        for key, dict_value in transition_dict.items():
            print(
                "Enter transitions for state {}.".format(key))

            for input_alphabet, transition_state in dict_value.items():
                transition_dict[key][input_alphabet] = input(
                    "CURRENT STATE : {}\tINPUT ALPHABET : {}\tNEXT STATE : ".format(key, input_alphabet))

        print("\nTRANSITION FUNCTION Q X SIGMA -> Q")
        print("CURRENT STATE\tINPUT ALPHABET\tNEXT STATE")
        for key, dict_value in transition_dict.items():
            for input_alphabet, transition_state in dict_value.items():
                print("{}\t\t{}\t\t{}".format(
                    key, input_alphabet, transition_state))

        return transition_dict

    # Functions to see if the dfa is accepted or rejected
    def run_state_transition(self, input_symbol):

        print("CURRENT STATE : {}\tINPUT SYMBOL : {}\t NEXT STATE : {}".format(
            self.CURRENT_STATE, input_symbol, self.DELTA[self.CURRENT_STATE][input_symbol]))
        self.CURRENT_STATE = self.DELTA[self.CURRENT_STATE][input_symbol]
        return self.CURRENT_STATE

    def check_if_accept(self):
        if self.CURRENT_STATE in self.acceptState:
            return True
        else:
            return False

    def run_machine(self, in_string):
        self.CURRENT_STATE = self.startState
        for ele in in_string:
            check_state = self.run_state_transition(ele)
        return self.check_if_accept()


if __name__ == "__main__":
    machine = DFA()
    input_string = list(input("Enter the input string : "))
    print("ACCEPTED" if machine.run_machine(input_string) else "REJECTED")
