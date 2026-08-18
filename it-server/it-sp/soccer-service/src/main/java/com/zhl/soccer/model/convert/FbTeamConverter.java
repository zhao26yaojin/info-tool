package com.zhl.soccer.model.convert;

import org.springframework.beans.BeanUtils;
import com.zhl.soccer.model.vo.FbTeamFbTeamVo;
import java.util.List;
import com.google.common.collect.Lists;
import com.zhl.soccer.model.entity.SpFbTeam;

public class FbTeamConverter {

	public static List<FbTeamFbTeamVo> entityListToVoList(List<SpFbTeam> fbTeamList){
		List<FbTeamFbTeamVo> teamVoList = Lists.newArrayList();

		for (SpFbTeam spFbTeam : fbTeamList) {
			if (spFbTeam == null) {
				return null;
			}
			FbTeamFbTeamVo fbTeamVo = entityToVo(spFbTeam);
			teamVoList.add(fbTeamVo);
		}

		return teamVoList;
	}

	public static FbTeamFbTeamVo entityToVo(SpFbTeam spFbTeam){
		FbTeamFbTeamVo fbTeamVo = new FbTeamFbTeamVo();

		if (spFbTeam == null) {
			return null;
		}
		BeanUtils.copyProperties(spFbTeam, fbTeamVo);

		return fbTeamVo;
	}

}