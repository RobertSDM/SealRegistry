from app.constants import APP_TITLE
from app.services.automation_service import Automation, Cordinate, Point
from app.services.cache_service import CacheService
from app.services.gui_service import InterGUI


def main():
    gui = InterGUI(APP_TITLE)

    # Get range
    start = gui.int_input_dialog("O número do lacre inicial")

    if start == None:
        return

    if start <= 0:
        gui.message_dialog("A posição INICIAL deve ser maior que '0'", "error")
        return

    end = gui.int_input_dialog("O número do lacre final (opcional)")

    if end == None:
        return
    
    if end > 0 and end < start:
        gui.message_dialog(
            "A posição FINAL deve ser maior que a posição INICIAL", "error"
        )
        return

    auto = Automation(gui)

    if CacheService.cache_exists() and gui.confirm_dialog(
        "Usar ultimas cordenadas?", "yesno"
    ):
        jcord = CacheService.read_cordinates()
        cord = Cordinate(
            start=Point(
                x=jcord["start"]["x"],
                y=jcord["start"]["y"],
            ),
            end=Point(
                x=jcord["end"]["x"],
                y=jcord["end"]["y"],
            ),
        )
    else:
        cord = auto.get_cordinates()
        CacheService.save_cordinates(
            {
                "start": {"x": cord.start.x, "y": cord.start.y},
                "end": {"x": cord.end.x, "y": cord.end.y},
            }
        )

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
