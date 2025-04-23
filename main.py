from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QStackedWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys


class WelcomeScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #2E2E2E; border-radius: 15px;")
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the Coffee Recommendation System ☕")
        welcome_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        welcome_label.setStyleSheet("color: #F8F8F8;")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(welcome_label)

        start_button = QPushButton("Start")
        start_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        start_button.setStyleSheet("background-color: #A67B5B; color: white; padding: 10px; border-radius: 10px;")
        start_button.clicked.connect(self.go_to_recommendation)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def go_to_recommendation(self):
        self.stacked_widget.setCurrentIndex(1)


class CoffeeRecommendationApp(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #2E2E2E; border-radius: 15px;")
        layout = QVBoxLayout()

        self.labels = {
            "strength": QLabel("How strong do you like your coffee?"),
            "milk": QLabel("How much milk do you prefer in your coffee?"),
            "sweet": QLabel("How sweet do you like your coffee?"),
            "flavor": QLabel("Do you prefer added flavors?"),
            "iced": QLabel("Do you like iced coffee?")
        }

        self.combos = {}
        options = ["Not at all", "Somewhat", "A lot"]
        for key, label in self.labels.items():
            label.setFont(QFont("Arial", 10))
            label.setStyleSheet("color: #F8F8F8;")
            layout.addWidget(label)

            combo = QComboBox()
            combo.addItems(options)
            combo.setFont(QFont("Arial", 10))
            combo.setStyleSheet("background-color: #D4A373; color: #2E2E2E; padding: 5px; border-radius: 10px;")
            self.combos[key] = combo
            layout.addWidget(combo)

        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.result_label.setStyleSheet("color: #F8F8F8; margin-top: 10px;")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        self.button = QPushButton("Get Recommendation")
        self.button.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.button.setStyleSheet("background-color: #A67B5B; color: white; padding: 10px; border-radius: 10px;")
        self.button.clicked.connect(self.get_recommendation)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_recommendation(self):
        choices = {key: self.combos[key].currentText().lower() for key in self.combos}
        coffee_recommendations = {
            ("a lot", "not at all", "not at all", "not at all", "not at all"): "Espresso - A strong, rich coffee.",
            ("a lot", "somewhat", "not at all", "not at all",
             "not at all"): "Cappuccino - Espresso with steamed milk and foam.",
            ("a lot", "somewhat", "somewhat", "not at all", "not at all"): "Mocha - Espresso with milk and chocolate.",
            ("somewhat", "somewhat", "somewhat", "somewhat",
             "not at all"): "Vanilla Latte - A smooth latte with vanilla flavor.",
            ("a lot", "not at all", "not at all", "not at all", "a lot"): "Iced Coffee - Chilled espresso over ice.",
            ("not at all", "not at all", "not at all", "not at all",
             "not at all"): "Americano - Diluted espresso for a balanced taste."
        }

        coffee = coffee_recommendations.get(
            tuple(choices.values()), "Americano - Diluted espresso for a balanced taste."
        )
        self.result_label.setText(f"☕ Recommended: {coffee}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    welcome_screen = WelcomeScreen(stacked_widget)
    recommendation_screen = CoffeeRecommendationApp(stacked_widget)

    stacked_widget.addWidget(welcome_screen)
    stacked_widget.addWidget(recommendation_screen)

    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    sys.exit(app.exec())
