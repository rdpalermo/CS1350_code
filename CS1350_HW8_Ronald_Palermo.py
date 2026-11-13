# 1. Exception_Lecture1 — practice_3_complete_pattern()
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("=" * 50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None

        try:
            file = open(filename, 'r')

        except FileNotFoundError:
            print(f"File '{filename}' not found")
            return None

        except PermissionError:
            print(f"No permission to read '{filename}'")
            return None

        else:
            content = file.read()
            processed_content = content.upper().split()
            return processed_content

        finally:
            if file:
                print("Closing file...")
                file.close()

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]

    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:

        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            if self.resource is not None:
                raise RuntimeError("Resource is already acquired")

            self.resource = f"{self.name} Resource"
            print(f"Acquired {self.name} resource")

        def release(self):
            """Release resource - must always happen."""
            if self.resource is not None:
                print(f"Released {self.name} resource")
                self.resource = None

        def use(self):
            """Use resource - only if acquired."""
            if self.resource is None:
                raise RuntimeError("Resource has not been acquired")

            print(f"Using {self.resource}")

    # Test resource management
    rm = ResourceManager("Database")

    try:
        rm.acquire()

    except RuntimeError as e:
        print(f"Resource error: {e}")

    else:
        rm.use()

    finally:
        rm.release()


# Run the practice
practice_3_complete_pattern()
###############################################################################
# 2. Exception_Lecture2 — practice_2_custom_exceptions()

def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "=" * 50)
    print("EXERCISE 5: Custom Exceptions")
    print("=" * 50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""

        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(
                f"Invalid move at {position}: {reason}"
            )

    class GameOverError(GameError):
        """Game has ended."""

        def __init__(self, winner):
            self.winner = winner
            super().__init__(f"Game over! Winner: {winner}")

    # TODO 2: Use custom exceptions
    class TicTacToe:

        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):

            if self.game_over:
                raise GameOverError("The game has already ended")

            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError(
                    (row, col),
                    "Position is out of bounds"
                )

            if self.board[row][col] != ' ':
                raise InvalidMoveError(
                    (row, col),
                    "Position is already taken"
                )

            self.board[row][col] = self.current_player

            # Check rows, columns, and diagonals for a winner
            player = self.current_player

            if (
                any(all(cell == player for cell in line)
                    for line in self.board)
                or any(
                    all(self.board[r][c] == player for r in range(3))
                    for c in range(3)
                )
                or all(self.board[i][i] == player for i in range(3))
                or all(self.board[i][2 - i] == player for i in range(3))
            ):
                self.game_over = True
                return

            # Check for a draw
            if all(cell != ' ' for row in self.board for cell in row):
                self.game_over = True
                return

            # Switch players
            self.current_player = 'O' if player == 'X' else 'X'

    # Test the game
    game = TicTacToe()

    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"Move ({row}, {col}) successful")

        except InvalidMoveError as e:
            print(f"Invalid move: {e}")

        except GameOverError as e:
            print(f"Game over: {e}")


# Run the practice
practice_2_custom_exceptions()
###############################################################################
# 3. Exception_Lecture2 — practice_3_complete_system()

def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    import os

    print("\n" + "=" * 50)
    print("EXERCISE 6: Complete Error Handler")
    print("=" * 50)

    # TODO: Build a file processing system with proper error handling
    class FileProcessor:

        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            file = None

            try:
                file = open(filename, 'r')
                content = file.read()

            except FileNotFoundError as e:
                print(f"File not found: {filename}")
                self.failed_files.append(filename)
                return None

            except PermissionError as e:
                print(f"Permission denied: {filename}")
                self.failed_files.append(filename)
                return None

            except Exception as e:
                print(f"Unexpected error processing {filename}: {e}")
                self.failed_files.append(filename)
                return None

            else:
                processed_content = content.upper()
                self.processed_files.append(filename)

                print(f"Successfully processed: {filename}")

                return processed_content

            finally:
                if file is not None:
                    file.close()
                    print(f"Closed file: {filename}")

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            try:
                files = os.listdir(directory)

            except FileNotFoundError:
                print(f"Directory not found: {directory}")
                self.failed_files.append(directory)
                return

            except PermissionError:
                print(f"Permission denied: {directory}")
                self.failed_files.append(directory)
                return

            except Exception as e:
                print(f"Error accessing directory: {e}")
                self.failed_files.append(directory)
                return

            for filename in files:
                filepath = os.path.join(directory, filename)

                if os.path.isfile(filepath):
                    self.process_file(filepath)

        def get_report(self):
            """
            Get processing report.
            """
            return {
                "total_processed": len(self.processed_files),
                "total_failed": len(self.failed_files),
                "processed_files": self.processed_files,
                "failed_files": self.failed_files
            }

    # Test the processor
    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")


# Run the practice
practice_3_complete_system()