import service from "@/utils/request"

export function getPage(params){
	return service({
		url: `/soccer/team/page`,
		method: "get",
		params: params
	})
}
