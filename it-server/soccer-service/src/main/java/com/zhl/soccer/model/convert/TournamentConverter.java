package com.zhl.soccer.model.convert;

import org.springframework.beans.BeanUtils;
import com.zhl.soccer.model.entity.FbTournament;
import java.util.List;
import com.google.common.collect.Lists;
import com.zhl.soccer.model.vo.TournamentVo;

public class TournamentConverter {

	public static List<TournamentVo> entityListToVoList(List<FbTournament> fbTournamentList){
		List<TournamentVo> tournamentVoList = Lists.newArrayList();

		for (FbTournament fbTournament : fbTournamentList) {
			if (fbTournament == null) {
				return null;
			}
			TournamentVo tournamentVo = entityToVo(fbTournament);
			tournamentVoList.add(tournamentVo);
		}

		return tournamentVoList;
	}

	public static TournamentVo entityToVo(FbTournament fbTournament){
		TournamentVo tournamentVo = new TournamentVo();

		if (fbTournament == null) {
			return null;
		}
		BeanUtils.copyProperties(fbTournament, tournamentVo);

		return tournamentVo;
	}

}