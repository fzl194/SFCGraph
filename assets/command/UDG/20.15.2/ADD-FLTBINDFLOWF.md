---
id: UDG@20.15.2@MMLCommand@ADD FLTBINDFLOWF
type: MMLCommand
name: ADD FLTBINDFLOWF（增加流过滤器的过滤器绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: FLTBINDFLOWF
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 300000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 流过滤器的过滤器绑定
status: active
---

# ADD FLTBINDFLOWF（增加流过滤器的过滤器绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于新增过滤器与流过滤器绑定关系，使用该过滤条件的业务可以成功匹配该流过滤器的L34层过滤条件。

## 注意事项

- 该命令执行后需要等待执行SET REFRESHSRV命令刷新后对新数据流生效。
- 该命令最大记录数为300000。当配置记录数大于规格的90%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格90%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 单个FlowFilter可以配置Filter和FilterIPv6总数为5000个。
- 该命令会导致用户匹配范围发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FLOWFILTER命令配置生成。 |
| FILTERNAME | 过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FILTER或者ADD FILTERIPV6命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FLTBINDFLOWF]] · 流过滤器的过滤器绑定关系（FLTBINDFLOWF）

## 关联任务

- [[UDG@20.15.2@Task@0-00008]]

## 使用实例

增加过滤器到流过滤器，FLOWFILTERNAME为“testflowfiltername”，FILTERNAME为“testfiltername”：

```
ADD FLTBINDFLOWF:FLOWFILTERNAME="testflowfiltername",FILTERNAME="testfiltername";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-FLTBINDFLOWF.md`
