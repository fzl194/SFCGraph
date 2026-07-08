---
id: UNC@20.15.2@MMLCommand@SET S1UBLACKLSTPARA
type: MMLCommand
name: SET S1UBLACKLSTPARA（设置S1-U黑名单参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: S1UBLACKLSTPARA
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1-U黑名单管理
- S1-U黑名单规则
status: active
---

# SET S1UBLACKLSTPARA（设置S1-U黑名单参数）

## 功能

**适用网元：MME**

暂不支持本命令。该命令用于设置S1-U黑名单参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SNDBLKLSTPLCY | 发送黑名单策略 | 可选必选说明：可选参数<br>参数含义：该参数控制系统在流程中接收到S-GW发送的消息中携带的S1-U IP地址为ADD S1UBLACKLST命令中配置的IP地址时，系统是否向eNodeB发送携带该IP地址的消息。<br>数据来源：整网规划<br>取值范围：<br>- “YES(发送)”<br>- “NO(不发送)”<br>默认值：无<br>系统初始设置值：YES(发送)<br>配置原则：当需要确保系统不向eNodeB发送携带S1-U黑名单IP地址的消息时，设置为NO（不发送）。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1UBLACKLSTPARA]] · S1-U黑名单参数（S1UBLACKLSTPARA）

## 使用实例

配置系统不向eNodeB发送携带S1-U黑名单IP地址的消息：

SET S1UBLACKLSTPARA: SNDBLKLSTPLCY=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-S1UBLACKLSTPARA.md`
