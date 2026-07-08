---
id: UNC@20.15.2@MMLCommand@RMV CTXSTARTRATING
type: MMLCommand
name: RMV CTXSTARTRATING（删除给OCS/CHF发送的消息初始携带的计费属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CTXSTARTRATING
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# RMV CTXSTARTRATING（删除给OCS/CHF发送的消息初始携带的计费属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除当前USERPROFILE下指定名字或者所有的计费属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CTXCHGPRMVT | 初始请求URR组删除类型 | 可选必选说明：必选参数<br>参数含义：指定CCR-Initial计费属性删除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：删除绑定的所有CCR-Initial计费属性。<br>- SPECIFIC：删除绑定的特定CCR-Initial计费属性。<br>默认值：无<br>配置原则：无 |
| CTXRURRGRPNAME | 初始请求URR组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CTXCHGPRMVT”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于指定CCR-Initial URR组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CTXSTARTRATING]] · 给OCS/CHF发送的消息初始携带的计费属性（CTXSTARTRATING）

## 使用实例

删除给OCS/CHF发送的消息初始携带的计费属性: USERPROFILENAME为TestUserProfileName，CTXCHGPRMVT为SPECIFIC，CTXRURRGRPNAME为TestCtxRChgProName：

```
RMV CTXSTARTRATING:USERPROFILENAME="TestUserProfileName", CTXCHGPRMVT=SPECIFIC, CTXRURRGRPNAME="TestCtxRChgProName";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除给OCS_CHF发送的消息初始携带的计费属性（RMV-CTXSTARTRATING）_09897212.md`
