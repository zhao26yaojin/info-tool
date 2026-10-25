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
import com.zhl.soccer.model.qo.TeamQo;
import com.zhl.soccer.model.vo.TeamVo;

@Service
public class TeamService extends ServiceImpl<TeamMapper, FbTeam> {

	public PageBean<TeamVo> selectVoPage(TeamQo teamQo, PageParam pageParam){
		LambdaQueryWrapper<FbTeam> lambdaQueryWrapper = baseMapper.getQueryWrapper(teamQo);

		Page<FbTeam> fbTeamPage = new Page<FbTeam>(pageParam.getCurrent(), pageParam.getSize());
		baseMapper.selectPage(fbTeamPage, lambdaQueryWrapper);
		List<TeamVo> teamVoList = TeamConverter.entityListToVoList(fbTeamPage.getRecords());
		PageBean<TeamVo> voPageBean = new PageBean<TeamVo>(pageParam.getCurrent(), pageParam.getSize(), fbTeamPage.getTotal(), teamVoList);
		return voPageBean;
	}

	public List<FbTeam> selectList(TeamQo teamQo){
		LambdaQueryWrapper<FbTeam> lambdaQueryWrapper = baseMapper.getQueryWrapper(teamQo);
		return this.list(lambdaQueryWrapper);
	}

}