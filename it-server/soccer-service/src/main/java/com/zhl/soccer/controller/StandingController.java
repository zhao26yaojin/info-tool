package com.zhl.soccer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import java.util.List;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.zhl.utils.rest.RestResponse;
import com.zhl.soccer.model.qo.StandingQo;
import com.zhl.soccer.service.StandingService;
import com.zhl.soccer.model.vo.StandingVo;

@RestController
@RequestMapping("/standing")
public class StandingController {

	@Autowired
	private StandingService standingService;

	@GetMapping("/list")
	public RestResponse<List<StandingVo>> List(StandingQo standingQo){
		List<StandingVo> standingVoList = standingService.selectVoList(standingQo);
		return RestResponse.ok(standingVoList);
	}

}