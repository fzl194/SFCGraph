---
id: UNC@20.15.2@MMLCommand@SET USRPDPCAP
type: MMLCommand
name: SET USRPDPCAP（设置用户面PDP规格表）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: USRPDPCAP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- PDP资源管理
- 用户面PDP规格管理
status: active
---

# SET USRPDPCAP（设置用户面PDP规格表）

## 功能

![](设置用户面PDP规格表(SET USRPDPCAP)_26305662.assets/notice_3.0-zh-cn_2.png)

配置过低会导致系统尚未达到真正的拥塞、过载时就不再允许新用户接入。

**适用网元：SGSN**

该命令用于设置GTP进程的PDP过载门限、PDP过载恢复门限、PDP拥塞门限、PDP拥塞恢复门限。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 本命令参数设置不当可能造成PDP无法激活，请谨慎修改。建议使用系统初始值。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCOPE | 操作范围 | 可选必选说明：必选参数<br>参数含义：该参数用于修改范围是整系统，还是针对指定的节点。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（整系统）”<br>系统初始设置值：<br>“ALL（整系统）”<br>。 |
| PDPBTHD | PDP数过载门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户面PDP数的过载门限，该参数用来上报告警（告警名称：用户资源过载，告警ID：80658）。<br>数据来源：本端规划<br>取值范围：0～100(%)，不包括100。<br>系统初始设置值：<br>“85”<br>。<br>配置原则：<br>“PDP数过载门限”<br>应大于<br>“PDP数过载恢复门限”<br>。<br>说明：当用户面PDP数所占的百分比大于等于该门限时会产生系统资源过载告警，但此时该GTP进程上还可以激活新的PDP上下文。 |
| PDPBRTHD | PDP数过载恢复门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户面PDP数过载恢复门限，该参数用来恢复上报告警(告警名称：用户资源过载，告警ID：80658)。<br>数据来源：本端规划<br>取值范围：0～100(%)，不包括100。<br>系统初始设置值：<br>“80”<br>。<br>配置原则：<br>“PDP数过载恢复门限”<br>应小于<br>“PDP数拥塞恢复门限”<br>。<br>说明：用户面PDP数过载后，当PDP数所占的百分比小于等于该门限时会恢复系统资源过载告警。 |
| PDPCTHD | PDP数拥塞门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户面PDP数拥塞门限，该参数用来上报告警（告警名称：用户资源拥塞，告警ID：80659）。<br>数据来源：本端规划<br>取值范围：0～100(%)，不包括0。<br>系统初始设置值：<br>“95”<br>。<br>配置原则：<br>“PDP数拥塞门限”<br>应大于<br>“PDP数过载门限”<br>。<br>说明：当用户面PDP数所占的百分比大于等于该门限时会产生系统资源拥塞告警，而且该GTP进程上不能再激活新的PDP上下文。 |
| PDPCRTHD | PDP数拥塞恢复门限（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户面PDP数拥塞恢复门限，该参数用来恢复上报告警（告警名称：用户资源拥塞，告警ID：80659）。<br>数据来源：本端规划<br>取值范围：0～100(%)，不包括100。<br>系统初始设置值：<br>“90”<br>。<br>配置原则：<br>“PDP数拥塞恢复门限”<br>应小于<br>“PDP数拥塞门限”<br>。<br>说明：用户面PDP数拥塞后，当PDP数所占的百分比小于等于该门限时会恢复系统资源拥塞告警。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRPDPCAP]] · 用户面PDP规格表（USRPDPCAP）

## 使用实例

配置PDP规格表中过载门限为80%，过载恢复门限为60%，拥塞门限为90%，拥塞恢复门限为85%：

SET USRPDPCAP: SCOPE=ALL, PDPBTHD=80, PDPBRTHD=60, PDPCTHD=90, PDPCRTHD=85;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-USRPDPCAP.md`
