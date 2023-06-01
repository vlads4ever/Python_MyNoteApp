from model.saving.json_adapter import JSONAdapter
from model.service import Service
from presenter_package.presenter_module import PresenterModule
from view.console_ui import ConsoleUI

if __name__ == '__main__':
    view = ConsoleUI()
    save_adapter = JSONAdapter()
    service = Service(save_adapter)
    presenter = PresenterModule(view, service)
    view.start()
