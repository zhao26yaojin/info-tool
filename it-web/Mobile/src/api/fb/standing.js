import { http } from "@/utils/http"

export function getList(standingQuery, params){
	return http({
		url: `/soccer/standing/list`,
		method: "get",
		params: params
	})
}
