from PyQt5.QtWidgets import (
   QApplication,
   QWidget,
   QTableWidget,
   QTableWidgetItem,
   QPushButton,
   QVBoxLayout,
   QLineEdit,
)
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

       # Filter and update table
       self.table.setRowCount(len(testcase_ids))
       for row, testcase_id in enumerate(testcase_ids):
           self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
           self.table.setItem(row, 1, QTableWidgetItem(testcase_id))

       # Create dictionary with serial numbers as keys and testcase IDs as values
       testcase_dict = {int(item.text()): item.text() for row in range(self.table.rowCount()) for item in [self.table.item(row, 0), self.table.item(row, 1)] if item.text()}

       # Show message for empty IDs if applicable
       if not testcase_dict:
           self.show_message("No valid testcase IDs provided!")

       # (Replace this with your actual testcase execution logic)
       # Simulate running testcases for demonstration
       for id in testcase_dict:
           print(f"Running testcase: {testcase_dict[id]}")
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
