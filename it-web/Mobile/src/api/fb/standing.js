import { http } from "@/utils/http"

export function getStandingList(standingStandingQuery, params){
	return http({
		url: `/soccer/standing/list`,
		method: "get",
		params: params
	})
}
