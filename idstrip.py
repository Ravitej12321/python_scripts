
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QLineEdit
import sys

class TestcaseForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Testcase Runner")
        self.resize(400, 300)

        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["S.no", "Testcase", "Status"])
        self.table.setRowCount(10)

        # Set default values in table
        for row in range(10):
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))

        # Create button
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_testcases)

        # Create input field for testcase IDs
        self.testcase_input = QLineEdit()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.testcase_input)
        layout.addWidget(self.run_button)
        self.setLayout(layout)

    def run_testcases(self):
        # Get testcase IDs from input field
        testcase_ids = self.testcase_input.text().split(",")

        # Remove empty IDs
        testcase_ids = [id.strip() for id in testcase_ids if id.strip()]

        # Extract filled testcase IDs
        filled_ids = []
        for row in range(self.table.rowCount()):
            if self.table.item(row, 1).text():
                filled_ids.append(self.table.item(row, 1).text())

        # Combine filled IDs with provided IDs
        testcase_ids += filled_ids

        # Create dictionary with unique IDs
        testcase_dict = {id: None for id in set(testcase_ids)}

        # Show message for empty IDs if applicable
        if not testcase_dict:
            self.show_message("No valid testcase IDs provided!")

        # (Replace this with your actual testcase execution logic)
        # Simulate running testcases for demonstration
        for id in testcase_dict:
            print(f"Running testcase: {id}")
            # Set status based on your logic
            testcase_dict[id] = "Passed"

        # Show message with results
        self.show_message(f"Testcases completed! Dictionary: {testcase_dict}")

    def show_message(self, message):
        # (Replace this with your preferred method for displaying messages)
        print(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestcaseForm()
    window.show()
    sys.exit(app.exec_())
