import shutil


def ft_tqdm(lst: range) -> None:

    # Get the terminal size
    terminal_shape = shutil.get_terminal_size()
    total_width = terminal_shape.columns

    total = len(lst)
    bar_w = total_width - 43  # Total Width - (Text Space)

    for i, item in enumerate(lst, start=1):
        percentage = (i / total) * 100  # Percentage: (current / total) * 100

        filled_lengh = int(bar_w * i / total)  # How many we filled yet
        last_char = '>' if i == total else ''
        bar = '=' * filled_lengh + ' ' * (bar_w - filled_lengh) + last_char

        print(f'\r{percentage:.0f}%|[{bar}]| {i}/{total}', end='')

        yield item
