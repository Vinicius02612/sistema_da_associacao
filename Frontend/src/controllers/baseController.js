import { API_URL } from "@/config";
export class BaseController {
  static refreshingTokens = false;
  static refreshTokensPromise = null;

	constructor(userStore) {	
		this.UserStore = userStore;
  	this.url = API_URL;
	}
  urlFull(uri) {
    return `${this.url}/v1${uri}`;
  }

  getHeaders() {
    const headers = {
      Accept: "application/json",
      "Content-Type": "application/json; charset=utf-8",
    };

    if (localStorage.getItem("token")) {
      const token = localStorage.getItem("token");
      headers.Authorization = `Bearer ${token}`;
    }
    return headers;
  }

  async _sendRequest(uri, method, body, retry = null) {
    try {
      const response = await fetch(this.urlFull(uri), {
        method: method,
        headers: this.getHeaders(),
        body: JSON.stringify(body),
      });
      if (!response.ok) {
        throw response;
      }
      let json = {};
      const bodyResponse = await response.text();
      if (bodyResponse) {
        json = JSON.parse(bodyResponse);
      }
      return {
        body: json,
        status: response.status,
        statusText: response.statusText,
      };
    } catch (error) {
      const retryInfo = retry || [uri, method, body];
      if (error.status) {
        let json = {};
        const bodyResponse = await error.text();
        if (bodyResponse) {
          json = JSON.parse(bodyResponse);
        }
        if (
          json?.message === "Please authenticate" &&
          uri !== "/auth/refresh-tokens"
        ) {
          if (!BaseController.refreshingTokens) {
            BaseController.refreshTokensPromise = this.refreshTokens();
            BaseController.refreshingTokens = true;
          }
          await BaseController.refreshTokensPromise;
          BaseController.refreshingTokens = false;
          return await this._sendRequest(
            retryInfo[0],
            retryInfo[1],
            retryInfo[2],
            retryInfo
          );
        }
        throw {
          body: json,
          status: error.status,
          statusText: error.statusText,
        };
      }
      throw error;
    }
  }

  async _get(uri) {
    return this._sendRequest(uri, "GET");
  }

  async _post(uri, body) {
    return this._sendRequest(uri, "POST", body);
  }

  async _delete(uri, body) {
    return this._sendRequest(uri, "DELETE", body);
  }

  async _put(uri, body) {
    return this._sendRequest(uri, "PUT", body);
  }

  async _patch(uri, body) {
    return this._sendRequest(uri, "PATCH", body);
  }

  async refreshTokens() {
    try {
      const token = localStorage.getItem("refresh-token");

			if (!token) return;

      const response = await this._post("/auth/refresh-tokens", { token });
      this.UserStore.setToken(response.body.tokens);
      return response;
    } catch (error) {
      if (error.body?.message === "Please authenticate") {
				setTimeout(() => {
					window.location.href = "/login";
				}, 3000);
      }
      throw error;
    }
  }
}

export default BaseController;