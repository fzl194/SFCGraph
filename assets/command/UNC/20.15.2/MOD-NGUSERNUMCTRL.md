---
id: UNC@20.15.2@MMLCommand@MOD NGUSERNUMCTRL
type: MMLCommand
name: MOD NGUSERNUMCTRL（修改5G接入用户数控制参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGUSERNUMCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 5G接入用户数控制
status: active
---

# MOD NGUSERNUMCTRL（修改5G接入用户数控制参数）

## 功能

![](修改5G接入用户数控制参数（MOD NGUSERNUMCTRL）_10097229.assets/notice_3.0-zh-cn_2.png)

执行该命令，ROAMNUMUPLIMIT参数设置不合理，可能会影响外网用户的接入。

**适用NF：AMF**

该命令用于修改指定Serving PLMN的5G接入用户数控制参数。

## 注意事项

修改接入用户数相关控制参数，仅对新接入用户生效，已接入用户不受影响。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数表示需要限制接入漫游用户数的Serving PLMN。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>PLMNIDX已通过ADD NGSRVPLMN进行配置。 |
| ROAMNUMUPLIMIT | 漫游用户接入数上限 | 可选必选说明：可选参数<br>参数含义：该参数用于限制指定Serving PLMN下允许接入的最大漫游用户数。<br>Serving PLMN下漫游用户数超过本参数的限制，拒绝新的漫游用户接入时，注册拒绝原因值受SET NGMMPROCTRL命令的ROAMRST参数控制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~8000000。<br>默认值：无<br>配置原则：<br>当漫游用户接入AMF时，漫游用户数会同时受特性License和本参数控制。License控制整系统的漫游用户数，本参数按ServingPLMN控制漫游用户数。<br>建议本参数的取值小于或等于特性License规格。<br>该命令下发后在20秒内生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGUSERNUMCTRL]] · 5G接入用户数控制参数（NGUSERNUMCTRL）

## 使用实例

索引为1的Serving PLMN的漫游用户接入数修改为20万，执行如下命令：

```
MOD NGUSERNUMCTRL:PLMNIDX=1,ROAMNUMUPLIMIT=200000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NGUSERNUMCTRL.md`
