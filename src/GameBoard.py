settings = {
            'timeout_turn': 0,
            'timeout_match': 0,
            'max_memory': 0,
            'time_left': 0,
            'game_type': 0,
            'rule': 0,
            'evaluate': 0,
            'folder': './'
            }

gameBoard_size = 19

def create(size):
    return [[0 for _ in range(size)] for _ in range(size)]