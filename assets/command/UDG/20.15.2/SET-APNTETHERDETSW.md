---
id: UDG@20.15.2@MMLCommand@SET APNTETHERDETSW
type: MMLCommand
name: SET APNTETHERDETSW（设置APN Tethering终端数量检测开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNTETHERDETSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- APN Tethering用户终端数量检测开关配置
status: active
---

# SET APNTETHERDETSW（设置APN Tethering终端数量检测开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来设置APN下Tethering终端数量检测开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 此命令的生效范围限于APN。
- 如果开关设置为继承，则继承SET TetherDetGlbSw命令的Switch参数配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SWITCH | 开关标识 | 可选必选说明：必选参数<br>参数含义：该参数用来配置Tethering用户终端数量检测功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：Tethering终端数量检测功能关闭。<br>- ENABLE：Tethering终端数量检测功能打开。<br>- INHERIT：继承全局缺省的Tethering终端数量检测开关状态。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNTETHERDETSW]] · APN Tethering终端数量检测开关（APNTETHERDETSW）

## 使用实例

假如运营商需使能名称为“huawei.com”的APN的Tethering终端数量检测功能：

```
SET APNTETHERDETSW: APN="huawei.com", SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APN-Tethering终端数量检测开关（SET-APNTETHERDETSW）_82837451.md`
