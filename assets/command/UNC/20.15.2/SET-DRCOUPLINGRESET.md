---
id: UNC@20.15.2@MMLCommand@SET DRCOUPLINGRESET
type: MMLCommand
name: SET DRCOUPLINGRESET（设置是否开启负荷分担容灾功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DRCOUPLINGRESET
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET DRCOUPLINGRESET（设置是否开启负荷分担容灾功能）

## 功能

![](设置是否开启负荷分担容灾功能（SET DRCOUPLINGRESET）_74474841.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，开启前请确认主备容灾已关闭，否则可能会导致业务呼损。请谨慎使用。

该命令用于设置是否开启负荷分担容灾功能。

## 注意事项

- 该命令执行后立即生效。

- 该命令只用于在UEG-M/UEG-L/UEG采用负荷分担容灾模式下执行。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| COUPLINGRESET |
| --- |
| NO |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COUPLINGRESET | 是否使能负荷分担容灾功能 | 可选必选说明：可选参数<br>参数含义：该参数用于是否使能负荷分担容灾功能。<br>数据来源：本端规划<br>取值范围：<br>- YES（是）<br>- NO（否）<br>默认值：NO。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRCOUPLINGRESET查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [负荷分担容灾功能开启信息（DRCOUPLINGRESET）](configobject/UNC/20.15.2/DRCOUPLINGRESET.md)

## 使用实例

设置是否开启负荷分担容灾功能：

```
%%SET DRCOUPLINGRESET: COUPLINGRESET=NO;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置是否开启负荷分担容灾功能（SET-DRCOUPLINGRESET）_74474841.md`
