from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "lobby", "product", "aggresive", "figure", "road", "skill", "grind", "brake"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "lobby",
                "conditions": "is_going_to_lobby",
            },
            {
                "trigger": "advance",
                "source": "product",
                "dest": "aggresive",
                "conditions": "is_going_to_aggresive",
            },
            {
                "trigger": "advance",
                "source": "product",
                "dest": "figure",
                "conditions": "is_going_to_figure",
            },
            {
                "trigger": "advance",
                "source": "product",
                "dest": "road",
                "conditions": "is_going_to_road",
            },
            {
                "trigger": "advance",
                "source": "skill",
                "dest": "brake",
                "conditions": "is_going_to_brake",
            },
            {
                "trigger": "advance",
                "source": "skill",
                "dest": "grind",
                "conditions": "is_going_to_grind",
            },
            {
                "trigger": "advance",
                "source": ["lobby","aggresive","figure","road","product","skill","grind","brake"],
                "dest": "lobby",
                "conditions": "is_going_back_lobby",
            },
            {
                "trigger": "advance",
                "source": ["aggresive","figure","road","product","lobby","grind","brake"],
                "dest": "skill",
                "conditions": "is_going_to_skill",
            },
            {
                "trigger": "advance",
                "source": ["aggresive","figure","road","lobby","skill","grind","brake"],
                "dest": "product",
                "conditions": "is_going_to_product",
            },
            {"trigger": "go_back", "source": ["aggresive","figure","road","product","skill","grind","brake"], "dest": "lobby"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine