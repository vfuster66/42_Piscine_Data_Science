from colorama import init, Fore, Style

init(autoreset=True)


class Printer:
    def success(self, message: str) -> None:
        print(Fore.GREEN + "✅ " + message)

    def error(self, message: str) -> None:
        print(Fore.RED + "❌ " + message)

    def info(self, message: str) -> None:
        print(Fore.YELLOW + "🔎 " + message)

    def title(self, title: str) -> None:
        print(Style.BRIGHT + Fore.CYAN + f"\n=== {title} ===")

    def header(self, header: str) -> None:
        print("\n" + Style.BRIGHT + Fore.MAGENTA + "=" * 50)
        print(Style.BRIGHT + Fore.CYAN + f"{header}")
        print(Style.BRIGHT + Fore.MAGENTA + "=" * 50)

    def footer(self, footer: str) -> None:
        print(Style.BRIGHT + Fore.MAGENTA + "=" * 50)
        print(Style.BRIGHT + Fore.CYAN + f"{footer}")
        print(Style.BRIGHT + Fore.MAGENTA + "=" * 50)

    def section(self, section_title: str) -> None:
        print("\n" + Style.BRIGHT + Fore.BLUE + f"--- {section_title} ---")

    def print_vector(self, vector, label: str = "Vector") -> None:
        print(Fore.YELLOW + f"{label}: {vector.values}")

    def print_matrix(self, matrix, label: str = "Matrix") -> None:
        print(Fore.YELLOW + f"{label}:")
        for row in matrix.values:
            print("   ", row)
