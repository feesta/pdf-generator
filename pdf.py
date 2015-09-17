from fpdf import FPDF
import math

class PDF(FPDF):
    def start(self, title, circles, lines):
        self.title = title
        self.circles = circles
        self.lines = lines

        self.alias_nb_pages()
        self.add_page()
        self.set_font('Times', '', 12)

        self.set_line_width(.1)

        for i in range(0, lines):
            y = 120 + i * 2
            x = 30
            x2 = x + 60
            self.line(x, y, x2, y)

        self.set_line_width(1)
        c = int(math.ceil(math.sqrt(circles)))
        count = 0
        for i in range(0, c):
            for j in range(0, c):
                x = 100 + j * 10
                y = 120 + i * 10
                self.ellipse(x, y, 10, 10)
                count += 1
                if count >= circles: break
            if count >= circles: break

    def save(self):
        filename = 'static/%s_%s_%s.pdf' % (self.title, self.circles, self.lines)
        self.output(filename, 'F')
        return filename

    def header(self):
        # Logo
        self.image('cat.jpg', 30, 30, 60)
        # Arial bold 15
        self.set_font('Arial', 'B', 25)
        # Move to the right
        self.ln(60)
        self.cell(120)
        # Title
        self.cell(30, 10, self.title, 0, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        pass

# Instantiation of inherited class
if __name__ == '__main__':
    pdf = PDF()
    pdf.start()
    pdf.save()
