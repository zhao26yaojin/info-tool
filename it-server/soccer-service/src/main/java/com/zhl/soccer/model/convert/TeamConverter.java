package com.zhl.soccer.model.convert;

import org.springframework.beans.BeanUtils;
import com.zhl.soccer.model.entity.FbTeam;
import java.util.List;
import com.google.common.collect.Lists;
import com.zhl.soccer.model.vo.TeamTeamVo;

public class TeamConverter {

	public static List<TeamTeamVo> entityListToVoList(List<FbTeam> fbTeamList){
		List<TeamTeamVo> teamVoList = Lists.newArrayList();

		for (FbTeam fbTeam : fbTeamList) {
			if (fbTeam == null) {
				return null;
			}
			TeamTeamVo teamTeamVo = entityToVo(fbTeam);
			teamVoList.add(teamTeamVo);
		}

		return teamVoList;
	}

	public static TeamTeamVo entityToVo(FbTeam fbTeam){
		TeamTeamVo teamTeamVo = new TeamTeamVo();

		if (fbTeam == null) {
			return null;
		}
		BeanUtils.copyProperties(fbTeam, teamTeamVo);

		return teamTeamVo;
	}

}