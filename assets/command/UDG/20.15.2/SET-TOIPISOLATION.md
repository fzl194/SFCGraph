---
id: UDG@20.15.2@MMLCommand@SET TOIPISOLATION
type: MMLCommand
name: SET TOIPISOLATION（设置IP地址隔离开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOIPISOLATION
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- IP地址隔离功能
status: active
---

# SET TOIPISOLATION（设置IP地址隔离开关）

## 功能

**适用NF：UPF**

该命令用于设置IP地址隔离开关。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 当UE地址和POD内部网络冲突时，需要开启IP地址隔离开关。
- 开启IP地址隔离开关后单POD性能下降5%左右。
- 修改IP地址隔离开关前，需要先关闭TCP优化功能，否则当前所有业务将会全部中断。地址隔离开关修改后，再重新开启TCP优化功能。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IPISOLATIONSWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPISOLATIONSWITCH | IP地址隔离功能开关 | 可选必选说明：必选参数<br>参数含义：设置IP地址隔离功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IP地址隔离功能配置（TOIPISOLATION）](configobject/UDG/20.15.2/TOIPISOLATION.md)

## 使用实例

开启IP地址隔离开关：

```
SET TOIPISOLATION: IPISOLATIONSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置IP地址隔离开关（SET-TOIPISOLATION）_59028942.md`
