---
id: UNC@20.15.2@MMLCommand@SET SGWCHARGECFG
type: MMLCommand
name: SET SGWCHARGECFG（SGW计费配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SGWCHARGECFG
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 对新用户生效
is_dangerous: true
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW计费基础参数
status: active
---

# SET SGWCHARGECFG（SGW计费配置）

## 功能

**适用NF：SGW-C**

![](SGW计费配置（SET SGWCHARGECFG）_09896989.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改配置可能导致无可用CG，SGW话单无法被正常处理，从而导致用户无法计费。

SET SGWCHARGECFG命令用来修改SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用PGW携带的CG。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | HOMEOFFLINE | ROAMOFFLINE | VISITOFFLINE | SGWCGFLAG |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | ENABLE | ENABLE | USE_LOCAL |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEOFFLINE | 本地用户离线计费开关 | 可选必选说明：可选参数<br>参数含义：本地用户离线计费开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：打开本地离线计费。<br>- DISABLE：关闭本地离线计费。 |
| ROAMOFFLINE | 漫游用户离线计费开关 | 可选必选说明：可选参数<br>参数含义：漫游用户离线计费开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：打开漫游离线计费。<br>- DISABLE：关闭漫游离线计费。 |
| VISITOFFLINE | 拜访用户离线计费开关 | 可选必选说明：可选参数<br>参数含义：拜访用户离线计费开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：打开拜访离线计费。<br>- DISABLE：关闭拜访离线计费。 |
| SGWCGFLAG | SGW CG IP选择 | 可选必选说明：可选参数<br>参数含义：SGW CG选择。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USE_LOCAL：使用本地CG IP。该参数使用ADD CG命令配置生成。<br>- USE_PGW：使用PGW携带的CG IP。<br>默认值：无<br>配置原则：<br>- USE_LOCAL：使用本地CG。该参数使用ADD CG命令配置生成。<br>- USE_PGW：使用PGW携带的CG。 |

## 操作的配置对象

- [SGW计费配置（SGWCHARGECFG）](configobject/UNC/20.15.2/SGWCHARGECFG.md)

## 使用实例

SGW计费配置，关闭本地离线计费，打开漫游离线计费，打开拜访离线计费，使用本地CG：

```
SET SGWCHARGECFG:HOMEOFFLINE=DISABLE,ROAMOFFLINE=ENABLE,VISITOFFLINE=ENABLE,SGWCGFLAG=USE_LOCAL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SGW计费配置（SET-SGWCHARGECFG）_09896989.md`
