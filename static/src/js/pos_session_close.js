odoo.define('pos_close_notification.pos_session_close', function (require) {
    "use strict";

    var bus = require('bus.bus').bus;

    bus.on('notification', this, function (notifications) {
        for (var notif of notifications) {
            if (notif[0][1] === 'pos.session_closed') {
                var session_info = notif[1];
                console.log('POS session closed: ', session_info.session_id);
                // Aquí puedes ejecutar cualquier acción que desees, por ejemplo:
                alert('La sesión de punto de venta ha sido cerrada.');
            }
        }
    });

    bus.startPolling();
});
