import {requestService} from "@/services/Request.service";
import {loginEndpoint} from "@/utils/constants";

export const userService = {
    postLogin,
    putApprove,
};

async function postLogin(name, password) {

    const payload = {
        name, password
    };


    const result = await requestService.post(loginEndpoint, payload);

    if (!result.ok) {
        console.warn('postLogin failed!')
        return {};
    }

    return await result.json();
}
// eslint-disable-next-line no-unused-vars
async function putApprove(photoId) {
    return true;
}

