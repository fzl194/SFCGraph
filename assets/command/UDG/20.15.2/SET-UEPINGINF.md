---
id: UDG@20.15.2@MMLCommand@SET UEPINGINF
type: MMLCommand
name: SET UEPINGINF（设置UE Ping逻辑接口开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UEPINGINF
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- UEPing逻辑接口控制
status: active
---

# SET UEPINGINF（设置UE Ping逻辑接口开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](设置UE Ping逻辑接口开关（SET UEPINGINF）_79568175.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，测试完成后，请及时删除该配置，否则存在安全风险。

该命令用于设置UE ping逻辑口的开关。如果开关使能，则系统会对UE ping逻辑口的报文回响应。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该配置通常用于网络测试场景，测试完成后，请及时删除该配置，否则存在安全风险。
- 逻辑口swmif不受该命令控制，默认按照DISABLE处理。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PINGSWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PINGSWITCH | Ping开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示UE ping逻辑口的使能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEPINGINF]] · UE Ping逻辑接口开关（UEPINGINF）

## 使用实例

将UE ping逻辑口的开关设置为使能：

```
SET UEPINGINF:PINGSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置UE-Ping逻辑接口开关（SET-UEPINGINF）_79568175.md`
