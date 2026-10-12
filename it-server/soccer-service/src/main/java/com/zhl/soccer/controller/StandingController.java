package com.zhl.soccer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import java.util.List;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.zhl.utils.rest.RestResponse;
import com.zhl.soccer.service.StandingService;
import com.zhl.soccer.model.qo.StandingStandingQo;
import com.zhl.soccer.model.vo.StandingStandingVo;

@RestController
@RequestMapping("/standing")
public class StandingController {

	@Autowired
	private StandingService standingService;

	@GetMapping("/standing/list")
	public RestResponse<List<StandingStandingVo>> standingList(StandingStandingQo standingStandingQo){
		List<StandingStandingVo> standingVoList = standingService.selectVoList(standingStandingQo);
		return RestResponse.ok(standingVoList);
	}

}