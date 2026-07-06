# Canonical Compound 登记表 — UDG@20.15.2
> 派生自 index.json compounds 段(spec §8.3)。Agent 复用查找用;人审通过的新 compound 自动入表(重跑 build_index.py 刷新)。
> compound 总数 4 | backbone(≥5 特性复用) 4 | 专用 0

## backbone(高频复用,≥5 特性)

### 1-00002 过滤链  (复用 8 特性)
- intent: 配置三四层/七层过滤器→聚合为FLOWFILTER→绑定（三四层FLTBINDFLOWF / 七层PROTBINDFLOWF）
- command_set: ADD FILTER, ADD FILTERIPV6, ADD FLOWFILTER, ADD FLTBINDFLOWF, ADD L7FILTER, ADD PROTBINDFLOWF
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00005, 2-00006, 2-00009, 2-00010

### 1-00003 规则与用户模板绑定  (复用 8 特性)
- intent: 配置规则ADD RULE→用户模板ADD USERPROFILE→绑定ADD RULEBINDING
- command_set: ADD RULE, ADD RULEBINDING, ADD USERPROFILE
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00005, 2-00006, 2-00009, 2-00010

### 1-00001 计费三件套  (复用 7 特性)
- intent: 配置 URR→URRGROUP→PCCPOLICYGRP 三级引用链，建立费率到策略组的绑定
- command_set: ADD PCCPOLICYGRP, ADD URR, ADD URRGROUP
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00006, 2-00009, 2-00010

### 1-00004 收尾  (复用 7 特性)
- intent: 配置缺省费率→（可选）防欺诈URR列表→刷新生效
- command_set: ADD SPECURRGRPLIST, SET REFRESHSRV, SET URRGRPBINDING
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00006, 2-00009, 2-00010

## 专用(单/少特性,<5)

