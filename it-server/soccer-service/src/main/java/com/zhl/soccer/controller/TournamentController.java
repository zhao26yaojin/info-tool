package com.zhl.soccer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import java.util.List;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.zhl.utils.rest.RestResponse;
import com.zhl.soccer.model.qo.TournamentQo;
import com.zhl.soccer.service.TournamentService;
import com.zhl.soccer.model.vo.TournamentVo;

@RestController
@RequestMapping("/tournament")
public class TournamentController {

	@Autowired
	private TournamentService tournamentService;

	@GetMapping("/list")
	public RestResponse<List<TournamentVo>> List(TournamentQo tournamentQo){
		List<TournamentVo> tournamentVoList = tournamentService.selectVoList(tournamentQo);
		return RestResponse.ok(tournamentVoList);
	}

}