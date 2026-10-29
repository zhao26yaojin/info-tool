import service from "@/utils/request"

export function getList(params){
	return service({
		url: `/soccer/tournament/list`,
		method: "get",
		params: params
	})
}
