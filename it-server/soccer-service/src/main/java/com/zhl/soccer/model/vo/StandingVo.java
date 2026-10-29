package com.zhl.soccer.model.vo;

import lombok.Data;
import java.lang.Integer;
import java.lang.Long;
import java.lang.String;

@Data
public class StandingVo {

	private Long id;

	private String teamLogo;

	private Long teamId;

	private String teamName;

	private Long tournamentId;

	private String sourceId;

	private Integer matches;

	private Integer wins;

	private Integer draws;

	private Integer losses;

	private Integer goalsFor;

	private Integer goalsAgainst;

	private Integer goalDifference;

	private Integer points;

}