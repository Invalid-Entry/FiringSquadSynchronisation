
class BAMCompilerError(Exception):
    pass

def BAMCompile(program):
    # generate 2 state machines, privates and generals
    private_program = {}
    general_program = {}
    
    lines = program.splitlines()
    in_state = False
    current_program = None
    current_state = None
    line_counter = 0
    
    try:
        for line in lines:
            line_counter += 1
            unstripped = line.strip()
            if len(unstripped) == 0 or unstripped[0] == "#": # Order of precidence matters
                # ignore line - comment or blacnk
                pass
            else:
                if unstripped == "-- BEGIN PRIVATE --":
                    current_program = private_program
                    in_state = False
                elif unstripped == "-- BEGIN GENERAL --":
                    current_program = general_program
                    in_state= False

                elif not in_state:
                    # this non comment line must be state definition
                    if unstripped[0] != line[0]:
                        raise BaMCompilerError("Line not a state declaration (Expecting one) line %s, %s" % (line_counter,line))
                    else:
                        in_state = True
                        current_state = {}
                        state_name = line.split(":")[0]
                        current_program[state_name] = current_state
                    
                else:
                    # in state, not in a comment or blank line
                    if unstripped[0] == line[0]:
                        # New state!
                        current_state = {}
                        state_name = unstripped.split(":")[0]
                        current_program[state_name] = current_state
                    else:
                        # its a programming line!
                        parts = unstripped.split()
                        
                        r = parts[0]
                        p = parts[1]
                        current_state[r] = p
                        
                        # if there isnt a 1 part then that will error out and be caught
                        
    except BaMCompilerError as e:
        raise e
    except Exception as e:
        message = "Unknown error on line %s\r\n%s\r\n" % (line_counter, line)
        raise BaMCompilerError(message, e)
    
    return general_program, private_program
        