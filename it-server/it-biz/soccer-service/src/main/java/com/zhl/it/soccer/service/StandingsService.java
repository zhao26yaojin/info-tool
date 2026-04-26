package com.zhl.it.soccer.service;

import com.zhl.it.soccer.model.entity.FbStandings;
import com.zhl.it.soccer.model.qo.StandingsQO;
import com.zhl.it.soccer.model.vo.StandingsVO;
import com.zhl.it.util.rest.PageBean;
import com.zhl.it.util.rest.PageParam;

import java.util.List;

public interface StandingsService {

    List<FbStandings> selectList(StandingsQO qo);

    List<StandingsVO> selectVOList(StandingsQO qo);

    PageBean<StandingsVO> selectVOPage(StandingsQO qo, PageParam pageParam);
}
