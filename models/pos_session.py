# models/pos_session.py
from odoo import models, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    def action_pos_session_closing_control(self):
        result = super(PosSession, self).action_pos_session_closing_control()
        for session in self:
            if session.state == 'closed':
                self.env['bus.bus']._sendone(
                    self.env.user.partner_id,
                    'pos.session_closed',
                    {'session_id': session.id}
                )
        return result
