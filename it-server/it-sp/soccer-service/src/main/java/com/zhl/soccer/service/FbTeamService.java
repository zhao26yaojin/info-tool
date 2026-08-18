package com.zhl.soccer.service;

import com.zhl.soccer.model.convert.FbTeamConverter;
import com.zhl.soccer.model.qo.FbTeamFbTeamQo;
import com.zhl.soccer.model.vo.FbTeamFbTeamVo;
import com.zhl.soccer.mapper.FbTeamMapper;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.util.List;
import org.springframework.stereotype.Service;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.zhl.soccer.model.entity.SpFbTeam;

@Service
public class FbTeamService extends ServiceImpl<FbTeamMapper, SpFbTeam> {

	public List<FbTeamFbTeamVo> selectVoList(FbTeamFbTeamQo fbTeamQo){
		List<SpFbTeam> fbTeamList = selectList(fbTeamQo);
		return FbTeamConverter.entityListToVoList(fbTeamList);
	}

	public List<SpFbTeam> selectList(FbTeamFbTeamQo fbTeamQo){
		LambdaQueryWrapper<SpFbTeam> lambdaQueryWrapper = baseMapper.getQueryWrapper(fbTeamQo);
		return this.list(lambdaQueryWrapper);
	}

}