# Assuming you're working with PyQt or PySide for GUI development:
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

# Create a widget (e.g., a dialog or main window)
widget = QWidget()

# Create a vertical layout to organize widgets
layout = QVBoxLayout()

# Add a label to the layout
label = QLabel("Number of sequences:")
layout.addWidget(label)

# Add the layout to the widget
widget.setLayout(layout)

# Show the widget (you'll need to add this to your application's main loop)
widget.show()
