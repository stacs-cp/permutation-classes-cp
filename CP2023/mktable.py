import xlsxwriter
import os

timeouts = {}
nodes = {}
counts = {}

sizes = set()
steps = set()
opts = set()

for f in os.listdir("infos"):
    base, _ = f.split(".")
    _, _, size, step, opt = base.split("-")
    sizes.add(int(size))
    steps.add(int(step))
    opts.add(opt)
    with open(f'infos/{f}', "r") as lines:
        for line in lines:
            k, v = line.strip().split(":")
            if k == "SolverTimeOut":
                timeouts[size, step, opt] = v
            if k == "SolverNodes":
                nodes[size, step, opt] = v
            if k == "SolverSolutionsFound":
                counts[size, step, opt] = v
    # infos[size, step, opt] =
    # print(size, step, opt)


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("CP2023-PP.xlsx")
worksheet = workbook.add_worksheet()

merge_format = workbook.add_format({'align': 'center'})
worksheet.merge_range(0, 0, 1, 0, 'Merged Cells', merge_format)
worksheet.merge_range(0, 1, 0, 4, 'Merged Cells', merge_format)
worksheet.merge_range(0, 5, 0, 8, 'Merged Cells', merge_format)

worksheet.write(0, 0, "Length")
worksheet.write(0, 1, "Number of permutations found")
worksheet.write(0, 5, "Number of search nodes required by Minion")

worksheet.write(1, 1, "Step 1")
worksheet.write(1, 2, "Step 2")
worksheet.write(1, 3, "Step 3")
worksheet.write(1, 4, "Step 4")

worksheet.write(1, 5, "Step 1")
worksheet.write(1, 6, "Step 2")
worksheet.write(1, 7, "Step 3")
worksheet.write(1, 8, "Step 4")

shaded = workbook.add_format()

shaded.set_bg_color('#D9D9D9')

for row_, size in enumerate(sorted(list(sizes))):
    row = row_ + 2
    worksheet.write(row, 0, size)

    for step in [1, 2, 3, 4]:
        key = str(size), str(step), "O0"
        try:
            if timeouts[key] == "1":
                worksheet.write(row, step, counts[key], shaded)
                worksheet.write(row, 4 + step, nodes[key], shaded)
            else:
                worksheet.write(row, step, counts[key])
                worksheet.write(row, 4 + step, nodes[key])
        except KeyError:
            pass

# # Widen the first column to make the text clearer.
# worksheet.set_column("A:A", 20)

# # Add a bold format to use to highlight cells.
# bold = workbook.add_format({"bold": True})

# # Write some simple text.
# worksheet.write("A1", "Hello")

# # Text with formatting.
# worksheet.write("A2", "World", bold)

# # Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)

workbook.close()
