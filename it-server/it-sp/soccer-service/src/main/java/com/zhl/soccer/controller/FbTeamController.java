package com.zhl.soccer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import com.zhl.soccer.model.qo.FbTeamFbTeamQo;
import com.zhl.soccer.model.vo.FbTeamFbTeamVo;
import com.zhl.soccer.service.FbTeamService;
import org.springframework.web.bind.annotation.GetMapping;
import java.util.List;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.zhl.utils.rest.RestResponse;

@RestController
@RequestMapping("/fbTeam")
public class FbTeamController {

	@Autowired
	private FbTeamService fbTeamService;

	@GetMapping("/fbTeam/list")
	public RestResponse<List<FbTeamFbTeamVo>> fbTeamList(FbTeamFbTeamQo fbTeamQo){
		List<FbTeamFbTeamVo> teamVoList = fbTeamService.selectVoList(fbTeamQo);
		return RestResponse.ok(teamVoList);
	}

}