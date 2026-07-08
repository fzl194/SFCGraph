---
id: UDG@20.15.2@MMLCommand@SET SRVCERTUPDCFG
type: MMLCommand
name: SET SRVCERTUPDCFG（设置证书更新拆链配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SRVCERTUPDCFG
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 证书更新拆链配置
status: active
---

# SET SRVCERTUPDCFG（设置证书更新拆链配置）

## 功能

**适用NF：UPF、PGW-U**

该命令用于设置证书更新拆链配置参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RBDLINKSW | RBDINTERVAL | RBDLINKNUM | RBDLINKDELAY |
| --- | --- | --- | --- | --- |
| 初始值 | ON | 4 | 10 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RBDLINKSW | 证书更新时拆链开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下更新证书，是否拆链。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：打开。<br>默认值：无<br>配置原则：无 |
| RBDINTERVAL | 单进程每批次拆链间隔（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下更新证书，每个进程每批次拆链的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是4~500，单位是秒。<br>默认值：无<br>配置原则：无 |
| RBDLINKNUM | 单进程每批次拆链数（条） | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下更新证书，每个进程每批次拆链数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~500，单位是条。<br>默认值：无<br>配置原则：无 |
| RBDLINKDELAY | 证书延迟拆链的时间(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下更新证书，每个进程每批次证书延迟拆链的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~10，单位为分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVCERTUPDCFG]] · 证书更新拆链配置（SRVCERTUPDCFG）

## 使用实例

假如需要设置证书更新拆链配置参数，则命令如下：

```
SET SRVCERTUPDCFG: RBDLINKSW=ON, RBDINTERVAL=4, RBDLINKNUM=10, RBDLINKDELAY=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SRVCERTUPDCFG.md`
