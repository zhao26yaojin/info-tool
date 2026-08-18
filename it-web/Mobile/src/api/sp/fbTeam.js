import { http } from "@/utils/http"

export function getFbTeamList(fbTeamFbTeamQuery, params){
	return http({
		url: `/soccer/fbTeam/list`,
		method: "get",
		params: params
	})
}
