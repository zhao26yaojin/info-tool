import service from "@/utils/request"

export function getList(params){
	return service({
		url: `/soccer/standing/list`,
		method: "get",
		params: params
	})
}
