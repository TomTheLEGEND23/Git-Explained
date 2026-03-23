def get_message() -> str:
	return "Hello from Git-Explained!" #change to break the Test :D


def get_status_message() -> str:
	return "Python setup and tests are working." 


def main() -> None:
	print(get_message())
	print(get_status_message())


if __name__ == "__main__":
	main()
