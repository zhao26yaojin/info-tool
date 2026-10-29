package com.zhl.soccer.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.apache.commons.collections4.CollectionUtils;
import java.util.stream.Collectors;
import com.zhl.soccer.model.entity.FbStanding;
import com.zhl.soccer.model.entity.FbTeam;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import java.util.List;
import java.lang.Long;
import java.util.Map;
import org.springframework.stereotype.Service;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.zhl.soccer.model.convert.StandingConverter;
import com.zhl.soccer.mapper.StandingMapper;
import com.zhl.soccer.model.qo.StandingQo;
import com.zhl.soccer.model.vo.StandingVo;
import com.zhl.soccer.model.qo.TeamQo;

@Service
public class StandingService extends ServiceImpl<StandingMapper, FbStanding> {

	@Autowired
	private TeamService teamService;

	public List<StandingVo> selectVoList(StandingQo standingQo){
		List<FbStanding> fbStandingList = selectList(standingQo);
		List<StandingVo> standingVoList = StandingConverter.entityListToVoList(fbStandingList);

		if (CollectionUtils.isNotEmpty(standingVoList)) {
			List<Long> teamIdList = standingVoList.stream().map(StandingVo::getTeamId).toList();

			TeamQo teamQo = new TeamQo();
			teamQo.setIdList(teamIdList);
			List<FbTeam> fbTeamList = teamService.selectList(teamQo);
			Map<Long, FbTeam> fbTeamMap = fbTeamList.stream().collect(Collectors.toMap(t -> t.getId(), t -> t));

			standingVoList.forEach(t -> {
				t.setTeamLogo(fbTeamMap.get(t.getTeamId()).getLogo());
				t.setTeamName(fbTeamMap.get(t.getTeamId()).getName());
			}

);
		}

		return standingVoList;
	}

	public List<FbStanding> selectList(StandingQo standingQo){
		LambdaQueryWrapper<FbStanding> lambdaQueryWrapper = baseMapper.getQueryWrapper(standingQo);
		return this.list(lambdaQueryWrapper);
	}

}