---
id: UNC@20.15.2@MMLCommand@RMV APNRDSCLIENTIP
type: MMLCommand
name: RMV APNRDSCLIENTIP（删除APN Radius Client IP接口）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNRDSCLIENTIP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- APN的Radius客户端地址属性
status: active
---

# RMV APNRDSCLIENTIP（删除APN Radius Client IP接口）

## 功能

**适用NF：PGW-C、SMF**

![](删除APN Radius Client IP接口（RMV APNRDSCLIENTIP）_09897363.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除Gi接口与APN实例的绑定关系，可能会导致发送鉴权或计费请求消息失败。

该命令用于解除APN实例所配置的radius client ip。当更改该APN实例下的配置时需要解除该APN与Gi接口的绑定关系，使用此命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定radius client ip需要绑定的APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：无 |
| AUTHORACCT | 鉴权或计费 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是鉴权时的radius client ip还是计费时的radius client ip。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。<br>- AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。<br>- ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。<br>默认值：无<br>配置原则：无 |
| INTFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该radius client ip配置在哪个接口上。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～13。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNRDSCLIENTIP]] · APN Radius Client IP接口（APNRDSCLIENTIP）

## 使用实例

- 当更改APN huawei.com下的配置时需要解绑定APN huawei.com下的鉴权请求消息的radius client ip，可按如下配置：
  ```
  RMV APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
  ```
- 当更改APN huawei.com下的配置时需要解绑定APN huawei.com下的计费请求消息的radius client ip，可按如下配置：
  ```
  RMV APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/0";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN-Radius-Client-IP接口（RMV-APNRDSCLIENTIP）_09897363.md`
