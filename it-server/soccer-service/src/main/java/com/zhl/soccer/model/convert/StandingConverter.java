package com.zhl.soccer.model.convert;

import org.springframework.beans.BeanUtils;
import com.zhl.soccer.model.entity.FbStanding;
import java.util.List;
import com.google.common.collect.Lists;
import com.zhl.soccer.model.vo.StandingVo;

public class StandingConverter {

	public static List<StandingVo> entityListToVoList(List<FbStanding> fbStandingList){
		List<StandingVo> standingVoList = Lists.newArrayList();

		for (FbStanding fbStanding : fbStandingList) {
			if (fbStanding == null) {
				return null;
			}
			StandingVo standingVo = entityToVo(fbStanding);
			standingVoList.add(standingVo);
		}

		return standingVoList;
	}

	public static StandingVo entityToVo(FbStanding fbStanding){
		StandingVo standingVo = new StandingVo();

		if (fbStanding == null) {
			return null;
		}
		BeanUtils.copyProperties(fbStanding, standingVo);

		return standingVo;
	}

}