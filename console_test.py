from robot import Robot, Direction, IllegalMoveException

bob = Robot()

bob.move()
bob.move()
bob.back_track()
state = bob.state()
print(state['direction'] == Direction.NORTH)
print(state['row'] == 9)
print(state['col'] == 1)
