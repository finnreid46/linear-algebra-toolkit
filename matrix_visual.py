import ast
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox


def validate_matrix(M, name="matrix"):
    if not isinstance(M, list) or not M or not all(isinstance(row, list) for row in M):
        raise ValueError(f"{name} must be a non-empty list of rows.")
    width = len(M[0])
    if width == 0 or any(len(row) != width for row in M):
        raise ValueError(f"{name} must be rectangular.")
    if not all(isinstance(x, (int, float)) for row in M for x in row):
        raise ValueError(f"{name} must contain only numbers.")
    return M


def parse_matrix(text, name):
    try:
        value = ast.literal_eval(text)
    except (SyntaxError, ValueError) as exc:
        raise ValueError(f"Could not parse {name}. Use syntax like [[1, 2], [3, 4]].") from exc
    return validate_matrix(value, name)


def j_th_column(M, j):
    return [row[j] for row in M]


def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError(
            f"Incompatible dimensions: A is {len(A)}x{len(A[0])}, "
            f"B is {len(B)}x{len(B[0])}."
        )

    result = []
    for row in A:
        result_row = []
        for j in range(len(B[0])):
            column = j_th_column(B, j)
            result_row.append(sum(a * b for a, b in zip(row, column)))
        result.append(result_row)
    return result


class MatrixMultiplicationVisual:
    def __init__(self):
        self.A = [[1, 2], [3, 4]]
        self.B = [[5, 6], [7, 8]]
        self.C = matrix_multiply(self.A, self.B)
        self.step = 0

        self.fig = plt.figure(figsize=(11, 7))
        self.fig.canvas.manager.set_window_title("Interactive Matrix Multiplication")

        self.ax_main = self.fig.add_axes([0.05, 0.25, 0.90, 0.68])
        self.ax_main.axis("off")

        ax_a = self.fig.add_axes([0.08, 0.13, 0.33, 0.055])
        ax_b = self.fig.add_axes([0.59, 0.13, 0.33, 0.055])
        self.box_a = TextBox(ax_a, "A = ", initial=str(self.A))
        self.box_b = TextBox(ax_b, "B = ", initial=str(self.B))

        ax_multiply = self.fig.add_axes([0.40, 0.04, 0.16, 0.06])
        ax_prev = self.fig.add_axes([0.18, 0.04, 0.12, 0.06])
        ax_next = self.fig.add_axes([0.66, 0.04, 0.12, 0.06])

        self.btn_multiply = Button(ax_multiply, "Multiply / Reset")
        self.btn_prev = Button(ax_prev, "Previous")
        self.btn_next = Button(ax_next, "Next")

        self.btn_multiply.on_clicked(self.reset)
        self.btn_prev.on_clicked(self.previous)
        self.btn_next.on_clicked(self.next)

        self.status = self.fig.text(0.5, 0.205, "", ha="center")
        self.draw()

    def reset(self, _event=None):
        try:
            A = parse_matrix(self.box_a.text, "A")
            B = parse_matrix(self.box_b.text, "B")
            C = matrix_multiply(A, B)
        except ValueError as exc:
            self.status.set_text(str(exc))
            self.fig.canvas.draw_idle()
            return

        self.A, self.B, self.C = A, B, C
        self.step = 0
        self.status.set_text("")
        self.draw()

    def previous(self, _event=None):
        self.step = max(0, self.step - 1)
        self.draw()

    def next(self, _event=None):
        max_step = len(self.A) * len(self.B[0]) - 1
        self.step = min(max_step, self.step + 1)
        self.draw()

    def _make_table(self, bbox, data, title, row_highlight=None, col_highlight=None):
        table = self.ax_main.table(
            cellText=data,
            cellLoc="center",
            loc="center",
            bbox=bbox,
        )
        table.auto_set_font_size(False)
        table.set_fontsize(12)

        for (r, c), cell in table.get_celld().items():
            selected = (
                (row_highlight is not None and r == row_highlight)
                or (col_highlight is not None and c == col_highlight)
            )
            cell.set_linewidth(3.0 if selected else 1.0)

        self.ax_main.text(
            bbox[0] + bbox[2] / 2,
            bbox[1] + bbox[3] + 0.04,
            title,
            ha="center",
            va="bottom",
            fontsize=14,
        )
        return table

    def draw(self):
        self.ax_main.clear()
        self.ax_main.axis("off")

        rows_c = len(self.A)
        cols_c = len(self.B[0])
        i = self.step // cols_c
        j = self.step % cols_c

        row = self.A[i]
        column = j_th_column(self.B, j)
        products = [a * b for a, b in zip(row, column)]
        value = sum(products)

        display_c = [["" for _ in range(cols_c)] for _ in range(rows_c)]
        completed = self.step + 1
        for k in range(completed):
            r = k // cols_c
            c = k % cols_c
            display_c[r][c] = self.C[r][c]

        self._make_table(
            [0.02, 0.48, 0.25, 0.30],
            self.A,
            "A",
            row_highlight=i,
        )
        self.ax_main.text(0.305, 0.63, "×", fontsize=24, ha="center", va="center")

        self._make_table(
            [0.34, 0.48, 0.25, 0.30],
            self.B,
            "B",
            col_highlight=j,
        )
        self.ax_main.text(0.625, 0.63, "=", fontsize=24, ha="center", va="center")

        self._make_table(
            [0.66, 0.48, 0.25, 0.30],
            display_c,
            "AB",
            row_highlight=i,
            col_highlight=j,
        )

        terms = " + ".join(f"{a}×{b}" for a, b in zip(row, column))
        self.ax_main.text(
            0.5,
            0.31,
            f"Entry ({i + 1}, {j + 1}):  {terms} = {value}",
            ha="center",
            va="center",
            fontsize=15,
        )
        self.ax_main.text(
            0.5,
            0.20,
            f"row {i + 1} of A  ·  column {j + 1} of B",
            ha="center",
            va="center",
            fontsize=12,
        )
        self.ax_main.text(
            0.5,
            0.09,
            f"Step {self.step + 1} of {rows_c * cols_c}",
            ha="center",
            va="center",
        )

        self.fig.canvas.draw_idle()


if __name__ == "__main__":
    MatrixMultiplicationVisual()
    plt.show()