package com.zhl.soccer.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.zhl.soccer.model.qo.FbTeamFbTeamQo;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.lang.Long;
import org.apache.ibatis.annotations.Mapper;
import com.zhl.soccer.model.entity.SpFbTeam;
import java.lang.String;
import org.apache.commons.lang3.StringUtils;
import com.baomidou.mybatisplus.core.toolkit.Wrappers;

@Mapper
public interface FbTeamMapper extends BaseMapper<SpFbTeam> {

	default LambdaQueryWrapper<SpFbTeam> getQueryWrapper(FbTeamFbTeamQo fbTeamQo){
		LambdaQueryWrapper<SpFbTeam> wrapper = Wrappers.lambdaQuery(SpFbTeam.class);
		wrapper.eq(fbTeamQo.getId() != null, SpFbTeam::getId, fbTeamQo.getId());
		wrapper.eq(StringUtils.isNotEmpty(fbTeamQo.getName()), SpFbTeam::getName, fbTeamQo.getName());
		wrapper.eq(fbTeamQo.getCountryId() != null, SpFbTeam::getCountryId, fbTeamQo.getCountryId());

		return wrapper;
	}

}