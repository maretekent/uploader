import IdleJS from 'idle-js';
import { getCookieValue } from '../utilities/cookie';


const IDLE_TIMEOUT_IN_MS = 3600000;
const AUTO_LOGOUT_URL = '/authentication/auto-logout/';


function idleCallback() {
    let csrfToken = getCookieValue(document.cookie, 'csrftoken');

    fetch(
        AUTO_LOGOUT_URL,
        {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'content-type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        }
    ).then( response => {
        if(response.status == 200) {
            window.location.reload();
        }
    });
}

function initialiseAutoLogoutWatcher() {
    let idle = new IdleJS({
        events: ['mousemove', 'keydown', 'mousedown', 'touchstart'],
        onIdle: idleCallback,
        idle: IDLE_TIMEOUT_IN_MS
    });

    idle.start();
}

initialiseAutoLogoutWatcher();
