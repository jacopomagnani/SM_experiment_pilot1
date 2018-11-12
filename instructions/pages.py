from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    pass


class Page2(Page):
    def vars_for_template(self):
        return {
            'rate_value': self.session.config['real_world_currency_per_point'],
            'fee': self.session.config['participation_fee'],
        }


class Page3(Page):
    pass


class Page4(Page):
    pass


class Page5(Page):
    pass


class Page6(Page):
    pass


class Page7(Page):
    pass


class Page8(Page):
    pass


page_sequence = [
    Page1,
    Page2,
    Page3,
    Page4,
    Page5,
    Page6,
    Page7,
    Page8
]
