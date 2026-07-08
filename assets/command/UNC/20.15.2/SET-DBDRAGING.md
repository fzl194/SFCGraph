---
id: UNC@20.15.2@MMLCommand@SET DBDRAGING
type: MMLCommand
name: SET DBDRAGING（设置CSDB容灾数据老化开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DBDRAGING
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# SET DBDRAGING（设置CSDB容灾数据老化开关）

## 功能

该命令用于设置CSDB容灾数据老化开关。此开关打开，本端残留的异地数据定期删除。此开关关闭，本端不处理残留的异地数据。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LDRINSTID | 本端容灾实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于指定本端容灾实例ID，可以通过<br>**[LST DRINST](查询容灾实例(LST DRINST)_51012924.md)**<br>命令查询获取，如果该命令查询结果为空，可以再通过<br>**[DSP DRINFO](查询容灾信息(DSP DRINFO)_51012929.md)**<br>命令查询获取。<br>数据来源：全网规划<br>取值范围：0～63。<br>默认值：无。 |
| PDRINSTID | 对端容灾实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于指定对端容灾实例ID，可以通过<br>**[LST DRCOMM](查询容灾实例地址(LST DRCOMM)_51012928.md)**<br>命令查询获取，如果该命令查询结果为空，可以再通过<br>**[DSP DRINFO](查询容灾信息(DSP DRINFO)_51012929.md)**<br>命令查询获取。<br>数据来源：全网规划<br>取值范围：0~63。<br>默认值：无。 |
| SWITCH | 容灾老化开关 | 可选必选说明：必选参数。<br>参数含义：该参数用于开启或关闭老化开关。<br>数据来源：本端规划<br>取值范围：<br>- “CLOSE_DR_AGING”：关闭容灾老化功能<br>- “OPEN_DR_AGING”：开启容灾老化功能<br>默认值：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DBDRAGING]] · CSDB容灾数据老化开关（DBDRAGING）

## 使用实例

打开 “本端容灾实例ID” 为 “0” ， “对端容灾实例ID” 为 “1” 的容灾老化开关：

```
SET DBDRAGING: LDRINSTID=0, PDRINSTID=1, SWITCH=OPEN_DR_AGING;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DBDRAGING.md`
