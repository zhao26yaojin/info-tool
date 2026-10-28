package com.zhl.soccer.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.zhl.soccer.model.entity.FbTournament;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import org.apache.ibatis.annotations.Mapper;
import com.zhl.soccer.model.qo.TournamentQo;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;

@Mapper
public interface TournamentMapper extends BaseMapper<FbTournament> {

	default LambdaQueryWrapper<FbTournament> getQueryWrapper(TournamentQo tournamentQo){
		LambdaQueryWrapper<FbTournament> wrapper = Wrappers.lambdaQuery(FbTournament.class);
		return wrapper;
	}

}