package com.zhl.soccer.service;

import com.zhl.soccer.model.entity.FbTournament;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.util.List;
import org.springframework.stereotype.Service;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.zhl.soccer.model.convert.TournamentConverter;
import com.zhl.soccer.mapper.TournamentMapper;
import com.zhl.soccer.model.qo.TournamentQo;
import com.zhl.soccer.model.vo.TournamentVo;

@Service
public class TournamentService extends ServiceImpl<TournamentMapper, FbTournament> {

	public List<TournamentVo> selectVoList(TournamentQo tournamentQo){
		List<FbTournament> fbTournamentList = selectList(tournamentQo);
		return TournamentConverter.entityListToVoList(fbTournamentList);
	}

	public List<FbTournament> selectList(TournamentQo tournamentQo){
		LambdaQueryWrapper<FbTournament> lambdaQueryWrapper = baseMapper.getQueryWrapper(tournamentQo);
		return this.list(lambdaQueryWrapper);
	}

}