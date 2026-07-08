---
id: UNC@20.15.2@MMLCommand@MOD N14N26INTOPPLCY
type: MMLCommand
name: MOD N14N26INTOPPLCY（修改N14N26接口跨运营商交互策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: N14N26INTOPPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF漫游功能控制
- N14N26接口跨运营商交互策略管理
status: active
---

# MOD N14N26INTOPPLCY（修改N14N26接口跨运营商交互策略）

## 功能

**适用NF：AMF**

该命令用于修改本AMF和指定运营商的AMF/MME之间的跨运营商交互策略。

## 注意事项

下一次移动性流程生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERMCC | 对端运营商移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制交互策略的对端运营商的Serving PLMN中的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| PEERMNC | 对端运营商移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要控制交互策略的对端运营商的Serving PLMN中的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| N14INTEROPPLCY | N14接口跨运营商交互策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在5G内移动性流程中，是否允许本AMF和指定运营商的AMF之间通过N14接口跨运营商传递用户上下文。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：无 |
| N26INTEROPPLCY | N26接口跨运营商交互策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在45G互操作流程中，是否允许本AMF和指定运营商的MME之间通过N26接口跨运营商传递用户上下文。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N14N26INTOPPLCY]] · N14N26接口跨运营商交互策略（N14N26INTOPPLCY）

## 使用实例

修改本AMF和运营商A之间的运营商交互策略，允许通过N14接口交互，执行如下命令：

```
MOD N14N26INTOPPLCY:PEERMCC="123",PEERMNC="45",N14INTEROPPLCY=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改N14N26接口跨运营商交互策略（MOD-N14N26INTOPPLCY）_75982856.md`
