package com.zhl.soccer.service;

import com.zhl.soccer.model.entity.FbStanding;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.util.List;
import org.springframework.stereotype.Service;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.zhl.soccer.model.convert.StandingConverter;
import com.zhl.soccer.mapper.StandingMapper;
import com.zhl.soccer.model.qo.StandingStandingQo;
import com.zhl.soccer.model.vo.StandingStandingVo;

@Service
public class StandingService extends ServiceImpl<StandingMapper, FbStanding> {

	public List<StandingStandingVo> selectVoList(StandingStandingQo standingStandingQo){
		List<FbStanding> fbStandingList = selectList(standingStandingQo);
		return StandingConverter.entityListToVoList(fbStandingList);
	}

	public List<FbStanding> selectList(StandingStandingQo standingStandingQo){
		LambdaQueryWrapper<FbStanding> lambdaQueryWrapper = baseMapper.getQueryWrapper(standingStandingQo);
		return this.list(lambdaQueryWrapper);
	}

}