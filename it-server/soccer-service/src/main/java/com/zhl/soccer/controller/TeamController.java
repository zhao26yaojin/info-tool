package com.zhl.soccer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import com.zhl.utils.rest.PageBean;
import com.zhl.utils.rest.PageParam;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.zhl.utils.rest.RestResponse;
import com.zhl.soccer.service.TeamService;
import com.zhl.soccer.model.qo.TeamTeamQo;
import com.zhl.soccer.model.vo.TeamTeamVo;

@RestController
@RequestMapping("/team")
public class TeamController {

	@Autowired
	private TeamService teamService;

	@GetMapping("/team/page")
	public RestResponse<PageBean<TeamTeamVo>> page(TeamTeamQo teamTeamQo, PageParam pageParam){
		PageBean<TeamTeamVo> voPageBean = teamService.selectVoPage(teamTeamQo, pageParam);
		return RestResponse.ok(voPageBean);
	}

}