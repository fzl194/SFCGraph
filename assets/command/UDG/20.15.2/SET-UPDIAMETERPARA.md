---
id: UDG@20.15.2@MMLCommand@SET UPDIAMETERPARA
type: MMLCommand
name: SET UPDIAMETERPARA（设置Diameter参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPDIAMETERPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- Diameter管理
- 路由控制
- Diameter路由控制
status: active
---

# SET UPDIAMETERPARA（设置Diameter参数）

## 功能

**适用NF：UPF**

该命令用于设置是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。

如果希望UPF在发送携带Destination-Host AVP的消息时，如果直连路径不存在或直连路径故障，尝试通过Destination-Realm来查找路由发送，则可将该参数使能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | REALMBASEROUTE |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMBASEROUTE | 基于域名的路由功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMETERPARA]] · Diameter参数（UPDIAMETERPARA）

## 使用实例

UPF在发送携带Destination-Host AVP的消息时，如果不存在到Destination-Host的直连路径，希望按照Destination-Realm来查找路由发送，则需要使能该功能：

```
SET UPDIAMETERPARA:REALMBASEROUTE=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置Diameter参数（SET-UPDIAMETERPARA）_97080173.md`
