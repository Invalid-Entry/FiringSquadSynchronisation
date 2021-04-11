import re
import copy

class RobotStateMachine():
    
    _current_state = None
    _machine_code = None
    
    def __init__(self, machine_code):
        self._machine_code = machine_code
        self._current_state = "0"
    
    def current_state(self):
        return self._current_state
    
    def tick(self, left_state, right_state):
        if not self._current_state in self._machine_code:
            # robot is stuck in this state until the end
            # but here for edge cases / programming
            #print('not finding a matching state')
            #print(self._current_state)
            #print('---')
            #print(self._machine_code)
            return
        current_logic = self._machine_code[self._current_state]
        
        target = "%s-%s" % (left_state, right_state)
        found = False
        for key,val in current_logic.items():
            try:
                if re.search(key, target):
                    found = True
                    break
            except Exception as e:
                raise Exception("Failed on %s" % key, e)
        if found:
            #print('chaning my state to %s' % val)
            self._current_state = val
           # print('not found match rule!')
        
        # if not found, maintain state
    
    def __str__(self):
        return str(self._current_state)

def construct_army(ar):
    mystr = ""
    for machine in ar:
        mystr += "%s" % str(machine)[0]
        
    return mystr

def tick_army(ar):
    states = []
    for machine in ar:
        states.append(machine.current_state())
    
    states = copy.deepcopy(states)

    for machineid in range(len(ar)):
        if machineid == 0:
            left = "-2"
            right = states[1]
        elif machineid == len(ar)-1:
            left= states[machineid-1]
            right = "-2"
        else:
            left= states[machineid-1]
            right = states[machineid+1]
        
        ar[machineid].tick(left,right)
        
def end_game_check(army):
    fire= False
    
    for machine in army:
        if machine._current_state == "BANG":
            fire = True
    
    return fire