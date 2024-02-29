package com.zhl.dt.soccer.controller;

import com.zhl.dt.soccer.model.qo.EventQO;
import com.zhl.dt.soccer.model.vo.EventVO;
import com.zhl.dt.soccer.service.EventService;
import com.zhl.dt.util.rest.RestResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Tag(name = "赛事模块")
@RestController
@RequestMapping("/event")
@Slf4j
public class EventController {

    @Autowired
    EventService eventService;

    @Operation(summary = "查询积分榜列表")
    @GetMapping("/list")
    public RestResponse<List<EventVO>> list(EventQO wordQO) {
        List<EventVO> voList = eventService.selectVOList(wordQO);

        return RestResponse.ok(voList);
    }
}
