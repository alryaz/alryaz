from typing import NamedTuple, Sequence


class ProjectType(NamedTuple):
    icon: str
    description: str


PROJECT_TYPE_HA = ProjectType(
    "https://www.home-assistant.io/images/home-assistant-logo.svg",
    "Home Assistant"
)
PROJECT_TYPE_PY = ProjectType(
    "https://www.python.org/static/community_logos/python-powered-h-50x65.png",
    "Python"
)


class ProjectItem(NamedTuple):
    user: str
    project: str
    type: ProjectType


class ProjectDefinition(NamedTuple):
    name_ru: str
    name_en: str
    items: Sequence[ProjectItem]


# noinspection PyArgumentList
PROJECTS = (
    ProjectDefinition(
        "Личный кабинет МосОблГаз",
        "Mosoblgaz Personal Cabinet",
        (ProjectItem("alryaz", "hass-mosoblgaz", PROJECT_TYPE_HA),)
    ),
    ProjectDefinition(
        "Личные кабинеты Энергосбыт Интер РАО",
        "Inter RAO Energosbyt Personal Cabinets",
        (ProjectItem("alryaz", "hass-lkcomu-interrao", PROJECT_TYPE_HA),
         ProjectItem("alryaz", "inter-rao-energosbyt-python", PROJECT_TYPE_PY))
    ),
    ProjectDefinition(
        "Личный кабинет ЭнергосбыТ Плюс",
        "EnergosbyT Plus",
        (ProjectItem("alryaz", "hass-energosbyt-plus", PROJECT_TYPE_HA),),
    ),
    ProjectDefinition(
        "Личные кабинеты ТНС Энерго",
        "TNS Energo Personal Cabinet",
        (ProjectItem("alryaz", "hass-tns-energo", PROJECT_TYPE_HA),
         ProjectItem("alryaz", "tns-energo-api", PROJECT_TYPE_PY)),
    ),
    ProjectDefinition(
        "Госуслуги Москвы",
        "Moscow PGU (state services)",
        (ProjectItem("alryaz", "hass-moscow-pgu", PROJECT_TYPE_HA),),
    ),
    ProjectDefinition(
        "Протокол Hekr",
        "Hekr Protocol",
        (ProjectItem("alryaz", "hass-hekr-component", PROJECT_TYPE_HA),
         ProjectItem("alryaz", "hekrapi-python", PROJECT_TYPE_PY)),
    ),
    ProjectDefinition(
        "Автомобильная сигнализация Pandora",
        "Pandora Car Alarm System",
        (ProjectItem("alryaz", "hass-pandora-cas", PROJECT_TYPE_HA),),
    ),
    ProjectDefinition(
        "Медиа-браузер Яндекс Музыки",
        "Yandex Music Media Browser",
        (ProjectItem("alryaz", "hass-yandex-music-browser", PROJECT_TYPE_HA),)
    ),
    ProjectDefinition(
        "Взаимодействие с устройствами Dahua",
        "Dahua devices communication",
        (ProjectItem("alryaz", "dahua-devices-python", PROJECT_TYPE_PY),)
    ),
    ProjectDefinition(
        "Устройства SNMP",
        "SNMP Devices",
        (ProjectItem("alryaz", "hass-component-snmp-device", PROJECT_TYPE_HA),)
    )
)

with open("README.md", "w", encoding="utf-8") as f:

    f.write("""## О себе / About me

> @TODO@

## Проекты / Projects
| Название | Ссылка |
| --- | --- |
""")
    
    for project_definition in PROJECTS:
        f.write(f"| {project_definition.name_ru} <br> {project_definition.name_en} | ")
        f.write(" <br> ".join(
            f"[<img src=\"{item.type.icon}\" width=\"16\" alt=\"{item.type.description}\"> "
            f"{item.user}/{item.project}](https://github.com/{item.user}/{item.project})"
            for item in project_definition.items
        ))
        f.write(" |\n")
