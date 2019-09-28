function getCookieValue(cookie, name) {
    return cookie
        .split(';')
        .map(entry => entry.split('=').map(item => item.trim()))
        .filter(entry => entry[0] === name)[0][1];
}

export { getCookieValue };
