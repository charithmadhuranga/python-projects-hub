from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Placeholder
from textual.containers import Container, Horizontal, Vertical


class Sidebar(Vertical):
    """A custom sidebar widget."""

    def compose(self) -> ComposeResult:
        yield Button("Dashboard", id="dash")
        yield Button("Settings", id="settings")
        yield Button("Logs", id="logs")


class MainApp(App):
    """The main application class."""

    CSS = """
    Screen {
        layout: horizontal;
    }
    Sidebar {
        width: 25;
        background: $panel;
        border-right: thin $primary;
    }
    #main-content {
        width: 1fr;
        padding: 1;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle Dark Mode"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Sidebar()
        with Container(id="main-content"):
            yield Static("Welcome to your Advanced TUI", id="title")
            yield Placeholder()
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


if __name__ == "__main__":
    app = MainApp()
    app.run()