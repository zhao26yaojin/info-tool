package com.zhl.soccer.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.zhl.soccer.model.entity.FbTeam;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.lang.Long;
import org.apache.ibatis.annotations.Mapper;
import java.lang.String;
import org.apache.commons.lang3.StringUtils;
import com.zhl.soccer.model.qo.TeamQo;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;

@Mapper
public interface TeamMapper extends BaseMapper<FbTeam> {

	default LambdaQueryWrapper<FbTeam> getQueryWrapper(TeamQo teamQo){
		LambdaQueryWrapper<FbTeam> wrapper = Wrappers.lambdaQuery(FbTeam.class);
		wrapper.eq(teamQo.getId() != null, FbTeam::getId, teamQo.getId());
		wrapper.eq(StringUtils.isNotEmpty(teamQo.getName()), FbTeam::getName, teamQo.getName());
		wrapper.eq(teamQo.getTournamentId() != null, FbTeam::getTournamentId, teamQo.getTournamentId());

		return wrapper;
	}

}