package com.zhl.soccer.service;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.zhl.soccer.model.entity.FbTeam;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.util.List;
import java.lang.Long;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.zhl.utils.rest.PageBean;
import com.zhl.utils.rest.PageParam;
import org.springframework.stereotype.Service;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.zhl.soccer.model.convert.TeamConverter;
import com.zhl.soccer.mapper.TeamMapper;
import com.zhl.soccer.model.qo.TeamTeamQo;
import com.zhl.soccer.model.vo.TeamTeamVo;

@Service
public class TeamService extends ServiceImpl<TeamMapper, FbTeam> {

	public PageBean<TeamTeamVo> selectVoPage(TeamTeamQo teamTeamQo, PageParam pageParam){
		LambdaQueryWrapper<FbTeam> lambdaQueryWrapper = baseMapper.getQueryWrapper(teamTeamQo);

		Page<FbTeam> fbTeamPage = new Page<FbTeam>(pageParam.getCurrent(), pageParam.getSize());
		baseMapper.selectPage(fbTeamPage, lambdaQueryWrapper);
		List<TeamTeamVo> teamVoList = TeamConverter.entityListToVoList(fbTeamPage.getRecords());
		PageBean<TeamTeamVo> voPageBean = new PageBean<TeamTeamVo>(pageParam.getCurrent(), pageParam.getSize(), fbTeamPage.getTotal(), teamVoList);
		return voPageBean;
	}

}