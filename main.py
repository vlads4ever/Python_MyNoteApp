from model_package.saving.json_adapter import JSONAdapter
from model_package.service import Service
from presenter_package.presenter import PresenterModule
from view_package.console_ui import ConsoleUI

if __name__ == '__main__':
    view = ConsoleUI()
    save_adapter = JSONAdapter()
    service = Service(save_adapter)
    presenter = PresenterModule(view, service)
    view.start()
