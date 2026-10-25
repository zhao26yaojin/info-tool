package com.zhl.soccer.model.convert;

import org.springframework.beans.BeanUtils;
import com.zhl.soccer.model.entity.FbTeam;
import java.util.List;
import com.google.common.collect.Lists;
import com.zhl.soccer.model.vo.TeamVo;

public class TeamConverter {

	public static List<TeamVo> entityListToVoList(List<FbTeam> fbTeamList){
		List<TeamVo> teamVoList = Lists.newArrayList();

		for (FbTeam fbTeam : fbTeamList) {
			if (fbTeam == null) {
				return null;
			}
			TeamVo teamVo = entityToVo(fbTeam);
			teamVoList.add(teamVo);
		}

		return teamVoList;
	}

	public static TeamVo entityToVo(FbTeam fbTeam){
		TeamVo teamVo = new TeamVo();

		if (fbTeam == null) {
			return null;
		}
		BeanUtils.copyProperties(fbTeam, teamVo);

		return teamVo;
	}

}