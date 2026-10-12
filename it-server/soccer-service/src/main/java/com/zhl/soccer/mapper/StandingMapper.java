package com.zhl.soccer.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.zhl.soccer.model.entity.FbStanding;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.lang.Long;
import org.apache.ibatis.annotations.Mapper;
import com.zhl.soccer.model.qo.StandingStandingQo;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;

@Mapper
public interface StandingMapper extends BaseMapper<FbStanding> {

	default LambdaQueryWrapper<FbStanding> getQueryWrapper(StandingStandingQo standingStandingQo){
		LambdaQueryWrapper<FbStanding> wrapper = Wrappers.lambdaQuery(FbStanding.class);
		wrapper.eq(standingStandingQo.getId() != null, FbStanding::getId, standingStandingQo.getId());
		wrapper.eq(standingStandingQo.getTournamentId() != null, FbStanding::getTournamentId, standingStandingQo.getTournamentId());

		return wrapper;
	}

}