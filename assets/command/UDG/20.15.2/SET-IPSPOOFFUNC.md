---
id: UDG@20.15.2@MMLCommand@SET IPSPOOFFUNC
type: MMLCommand
name: SET IPSPOOFFUNC（设置IP防护开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPSPOOFFUNC
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- IP Spoofing攻击防护
- IPSpoof攻击防护
status: active
---

# SET IPSPOOFFUNC（设置IP防护开关）

## 功能

**适用NF：UPF**

设置IP防护开关。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ANTISPOOFINGUL | ANTISPOOFINGDL |
| --- | --- | --- |
| 初始值 | ENABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ANTISPOOFINGUL | 上行IP防攻击开关 | 可选必选说明：可选参数<br>参数含义：上行IP防攻击开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ANTISPOOFINGDL | 下行IP防攻击开关 | 可选必选说明：可选参数<br>参数含义：下行IP防攻击开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSPOOFFUNC]] · 展示IP防攻击功能状态（IPSPOOFFUNC）

## 使用实例

假如运营商需要关闭IP防攻击检查，可以通过此命令配置：

```
SET IPSPOOFFUNC: ANTISPOOFINGUL=DISABLE, ANTISPOOFINGDL=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-IPSPOOFFUNC.md`
