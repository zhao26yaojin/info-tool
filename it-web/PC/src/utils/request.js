import axios from "axios"

const service = axios.create({
	baseURL: import.meta.env.VITE_BASE_API
})

const requestSuccess = config => {
	return config
}

const requestError = error => {
	return error
}
service.interceptors.request.use(requestSuccess, requestError)

const responseSuccess = response => {
	const resData = response.data

	if (resData.code != 200) {
		ElMessage.error(resData.message || "请求失败")

		return Promise.reject(resData)
	}


	return resData
}

const responseError = error => {
	return Promise.reject(error)
}
service.interceptors.response.use(responseSuccess, responseError)
export default service