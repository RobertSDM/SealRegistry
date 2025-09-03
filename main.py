from app.constants import APP_TITLE
from app.services.automation_service import Automation
from app.services.gui_service import InterGUI, MsgDialogType


def main():
    gui = InterGUI(APP_TITLE)

    # Get range
    start = gui.int_input_dialog("O número do lacre inicial")
    if start <= 0:
        gui.message_dialog("A posição INICIAL deve ser maior que '0'", "error")

        raise ValueError("The FINAL position needs to be greater than '0'")

    end = gui.int_input_dialog("O número do lacre final (opcional)")
    if end > 0 and end < start:
        gui.message_dialog(
            "A posição FINAL deve ser maior que a posição INICIAL", "error"
        )

        raise ValueError(
            "The FINAL position needs to be greater than the initial position"
        )

    auto = Automation(gui)

    if auto.cache_exists() and gui.confirm_dialog("Usar ultimas cordenadas?"):
        cord = auto.read_cordinates()
    else:
        cord = auto.get_cordinates()
        auto.save_cordinates(cord)

    if not cord:
        return

    if end == 0:
        invalid_seals = auto.automate(cord, start)
    else:
        invalid_seals = auto.automate(cord, start, end)

    if len(invalid_seals) > 0:
        gui.list_dialog("Lacres que não puderam ser cadastrados", invalid_seals)


if __name__ == "__main__":
    main()
