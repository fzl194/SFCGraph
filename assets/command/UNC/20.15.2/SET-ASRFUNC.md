---
id: UNC@20.15.2@MMLCommand@SET ASRFUNC
type: MMLCommand
name: SET ASRFUNC（设置容灾功能参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ASRFUNC
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 主备容灾管理
- 容灾功能参数
status: active
---

# SET ASRFUNC（设置容灾功能参数）

## 功能

![](设置容灾功能参数(SET ASRFUNC)_72345725.assets/notice_3.0-zh-cn_2.png)

该命令修改将启用或者关闭主备容灾功能，必须按照部署指导书中的步骤执行。

**适用网元：SGSN、MME**

该命令用于启用或者关闭网元的主备容灾功能。

现网 UNC 无法组POOL时，运营商可以选择两套 UNC 进行容灾，开启主备容灾功能。

两套 UNC 网元通过主备协商，确定运行主和运行备。主网元和备网元都配置相同的业务IP地址，主网元发布高优先级路由，备网元发布低优先级路由，控制业务只接入到主网元。

## 注意事项

- 该命令执行后立即生效。
- 系统初次运行时，会执行系统初始设置值。
- 该命令修改将启用或者关闭主备容灾功能，必须按照部署指导书中的步骤执行。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRSWITCH | 容灾功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元是否启用容灾功能。<br>数据来源：全网规划<br>取值范围：<br>- “ON（开启）”<br>- “OFF（关闭）”<br>系统初始设置值：OFF（关闭）<br>配置原则：现网<br>UNC<br>无法组POOL时，运营商可以启用主备容灾功能，提高可靠性。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ASRFUNC]] · 容灾功能参数（ASRFUNC）

## 使用实例

设置配置容灾功能， “容灾功能开关” 为 “开启” ：

SET ASRFUNC:GRSWITCH=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ASRFUNC.md`
