from shiny import App, ui, render
import sys
import importlib.util

# Check if our test package is installed
def is_package_installed(package_name):
    try:
        spec = importlib.util.find_spec(package_name)
        return spec is not None
    except:
        return False

app_ui = ui.page_fluid(
    ui.h2("Test Package Status"),
    ui.panel_well(
        ui.h3("Package Checker"),
        ui.p("This app checks if the dummy test package is installed."),
        ui.markdown("""
        ### Expected files in a dummy package:
        - `setup.py` - Package installation script
        - `dummy_pkg/__init__.py` - Makes the directory a package
        - `dummy_pkg/core.py` - Main functionality (empty in this case)
        """)),
    ui.hr(),
    ui.h3("Installation Status:"),
    ui.output_text("package_status"),
    ui.output_ui("installation_instructions")
)

def server(input, output, session):
    
    @render.text
    def package_status():
        if is_package_installed("dummy_pkg"):
            return "✅ The dummy_pkg is INSTALLED"
        else:
            return "❌ The dummy_pkg is NOT INSTALLED"
    
    @render.ui
    def installation_instructions():
        if not is_package_installed("dummy_pkg"):
            return ui.div(
                ui.p("To install the package, follow these steps:"),
                ui.tags.ol(
                    ui.tags.li("Download the package files"),
                    ui.tags.li("Navigate to the directory containing setup.py"),
                    ui.tags.li("Run: pip install -e .")
                )
            )
        else:
            return ui.div(
                ui.p("You can import the package with:"),
                ui.verbatim("import dummy_pkg"),
                ui.p("It doesn't do anything, but it exists!")
            )

app = App(app_ui, server)
