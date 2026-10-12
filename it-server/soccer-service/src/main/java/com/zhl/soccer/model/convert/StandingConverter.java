package com.zhl.soccer.model.convert;

import org.springframework.beans.BeanUtils;
import com.zhl.soccer.model.entity.FbStanding;
import java.util.List;
import com.google.common.collect.Lists;
import com.zhl.soccer.model.vo.StandingStandingVo;

public class StandingConverter {

	public static List<StandingStandingVo> entityListToVoList(List<FbStanding> fbStandingList){
		List<StandingStandingVo> standingVoList = Lists.newArrayList();

		for (FbStanding fbStanding : fbStandingList) {
			if (fbStanding == null) {
				return null;
			}
			StandingStandingVo standingStandingVo = entityToVo(fbStanding);
			standingVoList.add(standingStandingVo);
		}

		return standingVoList;
	}

	public static StandingStandingVo entityToVo(FbStanding fbStanding){
		StandingStandingVo standingStandingVo = new StandingStandingVo();

		if (fbStanding == null) {
			return null;
		}
		BeanUtils.copyProperties(fbStanding, standingStandingVo);

		return standingStandingVo;
	}

}