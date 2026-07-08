---
id: UDG@20.15.2@MMLCommand@ACT DEVVERIFICATION
type: MMLCommand
name: ACT DEVVERIFICATION（触发设备对账）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: DEVVERIFICATION
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 设备管理
status: active
---

# ACT DEVVERIFICATION（触发设备对账）

## 功能

该命令用于触发设备对账。当设备订阅信息或者属性信息发生异常时，可以使用该命令触发设备对账进行恢复。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VERIFYTYPE | 对账类型 | 可选必选说明：必选参数<br>参数含义：用于表示对账的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SUB：订阅信息。<br>- ATTR：属性信息。<br>默认值：无 |
| SRCPID | 源组件ID | 可选必选说明：必选参数<br>参数含义：用于表示对账的源组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| DSTPID | 目的组件ID | 可选必选说明：必选参数<br>参数含义：用于表示对账的目的组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| DEVID | 设备ID | 可选必选说明：条件可选参数，该参数在<br>“VERIFYTYPE”<br>配置为<br>“ATTR”<br>时为可选参数。<br>参数含义：用于表示对账的设备ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| ATTRID | 属性ID | 可选必选说明：条件可选参数，该参数在<br>“VERIFYTYPE”<br>配置为<br>“ATTR”<br>时为可选参数。<br>参数含义：用于表示对账的目的属性ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [触发设备对账（DEVVERIFICATION）](configobject/UDG/20.15.2/DEVVERIFICATION.md)

## 使用实例

- 对账订阅信息，指定源组件ID为FB0005，目的组件ID为80FC0012：
  ```
  ACT DEVVERIFICATION:VERIFYTYPE=SUB,SRCPID="FB0005",DSTPID="80FC0012"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
- 对账属性信息，指定源组件ID为80FC0012，目的组件ID为FB0005：
  ```
  ACT DEVVERIFICATION:VERIFYTYPE=ATTR,SRCPID="80FC0012",DSTPID="FB0005"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
- 对账属性信息，指定源组件ID为80FC0012，目的组件ID为FB0005，指定设备对象和设备属性：
  ```
  ACT DEVVERIFICATION:VERIFYTYPE=ATTR,SRCPID="80FC0012",DSTPID="FB0005",DEVID="9",ATTRID="172"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/触发设备对账（ACT-DEVVERIFICATION）_59103469.md`
