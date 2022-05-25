export const requestService = {
    get,
    post,
    put,
};

const baseUrl = 'http://localhost:5000';

function buildHeaders(use_multipart = false) {
    const headers = {
        'Authorization': localStorage.getItem('authToken') ?? '',
    };

    // MultiPart needs to be sent without header Content-Type header
    if (!use_multipart) {
        headers['Content-Type'] = 'application/json';
    }

    return headers;
}

async function get(endpoint) {
    try {
        return await fetch(`${baseUrl}${endpoint}`, {
            headers: buildHeaders(),
            method: 'GET',
        });
    } catch (e) {
        console.warn(`Request to ${endpoint} failed with ${JSON.stringify(e)}`)
        return {ok: false}
    }
}

async function put(endpoint, body) {
    try {
        return await fetch(`${baseUrl}${endpoint}`, {
            body: JSON.stringify(body),
            headers: buildHeaders(),
            method: 'PUT',
        });
    } catch (e) {
        console.warn(`Request to ${endpoint} failed with ${JSON.stringify(e)}`)
        return {ok: false}
    }
}

async function post(endpoint, body, use_multipart = false) {
    try {
        return await fetch(`${baseUrl}${endpoint}`, {
            body: use_multipart ? body : JSON.stringify(body),
            headers: buildHeaders(use_multipart),
            method: 'POST',
        });
    } catch (e) {
        console.warn(`Request to ${endpoint} failed with ${JSON.stringify(e)}`)
        return {ok: false}
    }

}

