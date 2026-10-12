package com.zhl.soccer.model.vo;

import lombok.Data;
import java.lang.Long;
import java.lang.String;

@Data
public class TeamTeamVo {

	private Long id;

	private String name;

	private String sourceId;

	private String logo;

	private Long tournamentId;

}