package com.zhl.soccer.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.zhl.soccer.model.entity.FbTeam;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.lang.Long;
import org.apache.ibatis.annotations.Mapper;
import java.lang.String;
import org.apache.commons.lang3.StringUtils;
import com.zhl.soccer.model.qo.TeamTeamQo;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;

@Mapper
public interface TeamMapper extends BaseMapper<FbTeam> {

	default LambdaQueryWrapper<FbTeam> getQueryWrapper(TeamTeamQo teamTeamQo){
		LambdaQueryWrapper<FbTeam> wrapper = Wrappers.lambdaQuery(FbTeam.class);
		wrapper.eq(teamTeamQo.getId() != null, FbTeam::getId, teamTeamQo.getId());
		wrapper.eq(StringUtils.isNotEmpty(teamTeamQo.getName()), FbTeam::getName, teamTeamQo.getName());
		wrapper.eq(teamTeamQo.getTournamentId() != null, FbTeam::getTournamentId, teamTeamQo.getTournamentId());

		return wrapper;
	}

}