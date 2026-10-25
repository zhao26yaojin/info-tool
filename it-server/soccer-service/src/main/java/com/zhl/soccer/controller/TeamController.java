package com.zhl.soccer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import com.zhl.utils.rest.PageBean;
import com.zhl.utils.rest.PageParam;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.zhl.utils.rest.RestResponse;
import com.zhl.soccer.model.qo.TeamQo;
import com.zhl.soccer.service.TeamService;
import com.zhl.soccer.model.vo.TeamVo;

@RestController
@RequestMapping("/team")
public class TeamController {

	@Autowired
	private TeamService teamService;

	@GetMapping("/page")
	public RestResponse<PageBean<TeamVo>> page(TeamQo teamQo, PageParam pageParam){
		PageBean<TeamVo> voPageBean = teamService.selectVoPage(teamQo, pageParam);
		return RestResponse.ok(voPageBean);
	}

}