import {requestService} from "@/services/Request.service";
import {photoApproveEndpoint, photoReactionsEndpoint, photosEndpoint} from "@/utils/constants";

export const photoService = {
    getPhotos,
    postPhoto,
    putLike,
    putComment,
    putApprove,
};

async function getPhotos() {
    const result = await requestService.get(photosEndpoint);

    if (!result.ok) {
        console.warn('getPhotos failed!')
        return [];
    }

    return await result.json();
}

async function postPhoto(
    description,
    author,
    file
) {

    const payload = new FormData();

    payload.append( 'description', description );
    payload.append( 'author', author );
    payload.append( 'file', file );

    const result = await requestService.post(photosEndpoint, payload, true);

    if (!result.ok) {
        console.warn('postPhoto failed!');
        return false;
    }
    return await result.json();
}

async function putLike(id) {
    const reactionsEndpoints = photoReactionsEndpoint.replace('<photo_id>', id);

    const payload = {
        'like': true,
    };

    const result = await requestService.put(reactionsEndpoints, payload);

    if (!result.ok) {
        console.warn('putLike failed!');
        return false;
    }

    return true;
}


async function putComment(id, comment) {
    const reactionsEndpoints = photoReactionsEndpoint.replace('<photo_id>', id);

    const payload = {
        'comment': comment,
    };

    const result = await requestService.put(reactionsEndpoints, payload);

    if (!result.ok) {
        console.warn('putLike failed!');
        return false;
    }

    return true;
}


async function putApprove(id, isApproved) {
    const reactionsEndpoints = photoApproveEndpoint.replace('<photo_id>', id);

    const payload = {
        'approve': isApproved,
    };

    const result = await requestService.put(reactionsEndpoints, payload);

    if (!result.ok) {
        console.warn('putApprove failed!');
        return false;
    }

    return true;
}

