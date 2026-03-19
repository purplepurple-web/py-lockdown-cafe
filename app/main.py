from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Нет вакцины")

        v_info = visitor["vaccine"]
        exp_date = v_info.get("expiration_date")
        if exp_date and exp_date < date.today():
            raise OutdatedVaccineError("Вакцина просрочена")

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Маска обязательна")

        return "Welcome to {}".format(self.name)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return "Friends should buy {} masks".format(masks_to_buy)

    return "Friends can go to {}".format(cafe.name)
