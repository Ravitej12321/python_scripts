import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFileDialog,
    QLabel,
    QProgressBar,
    QThread,
    pyqtSignal
)
from PyQt5.QtCore import Qt


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python File Execution")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.create_layout()
        self.create_connections()

    def create_layout(self):
        layout = QVBoxLayout(self.central_widget)

        # File selection
        file_select_layout = QHBoxLayout()
        layout.addLayout(file_select_layout)

        self.file_label = QLabel("No file selected")
        file_select_layout.addWidget(self.file_label)

        self.select_button = QPushButton("Select File")
        file_select_layout.addWidget(self.select_button)

        # Progress bar
        progress_layout = QHBoxLayout()
        layout.addLayout(progress_layout)

        self.progress_bar = QProgressBar()
        progress_bar.setMinimum(0)
        progress_bar.setMaximum(100)
        progress_layout.addWidget(self.progress_bar)

        # Run button
        self.run_button = QPushButton("Run")
        layout.addWidget(self.run_button)

        # Set initial state
        self.run_button.setEnabled(False)  # Disable until a file is selected

    def create_connections(self):
        self.select_button.clicked.connect(self.select_file)
        self.run_button.clicked.connect(self.run_script)

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Python File", "", "*.py"
        )
        if filename:
            self.file_label.setText(filename)
            self.run_button.setEnabled(True)  # Enable Run button after selection
        else:
            self.file_label.setText("No file selected")
            self.run_button.setEnabled(False)  # Disable Run button if no file selected

    def run_script(self):
        # Create a separate thread for execution
        self.thread = QThread()
        self.worker = ScriptRunner(self.file_label.text())  # Pass filename to worker
        self.worker.moveToThread(self.thread)

        # Connect signals for progress and error handling
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.handle_finished)
        self.worker.error.connect(self.handle_error)

        self.thread.started.connect(self.worker.run)  # Start thread
        self.thread.start()

        # Disable Run button and show progress bar
        self.run_button.setEnabled(False)
        self.progress_bar.setValue(0)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def handle_finished(self):
        self.thread.quit()
        self.thread.wait()
        self.run_button.setEnabled(True)  # Enable Run button after execution

    def handle_error(self, message):
        # Handle execution errors gracefully (e.g., display a message box)
        self.run_button.setEnabled(True)  # Enable Run button even on errors
        print(f"An error occurred: {message}")


class ScriptRunner(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        try:
            # Execute the Python script (replace this with your actual execution logic)
            with open(self.filename, 'r') as f:
                code = f.read()
            exec(code)
            self.progress.emit(100)
            self.finished.emit
