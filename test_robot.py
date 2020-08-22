import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.NORTH


def test_illegal_move(robot):
    robot.turn();
    robot.turn();

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_back_track_without_history(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 10
    assert state['col'] == 2

def test_illegal_move_south(robot):
    robot.turn()
    robot.move()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.SOUTH
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_move_west(robot):
    robot.turn()
    robot.move()
    robot.turn()
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.WEST
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1

def test_illegal_move_north(robot):
    state = robot.state()
    while state['row'] != 1:
        robot.move()
        state = robot.state()
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_move_east(robot):
    robot.turn()
    state = robot.state()
    while state['col'] != 10:
        robot.move()
        state = robot.state()
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_move_south(robot):
    robot.move()
    robot.turn()
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['direction'] == Direction.SOUTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_backtrack_making_move(robot):
    robot.move()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_backtrack_make_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_backtrack_make_multiple_moves(robot):
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1

def test_backtrack_all_multiple_moves_after_multiple_moves(robot):
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1