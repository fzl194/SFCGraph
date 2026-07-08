---
id: UNC@20.15.2@MMLCommand@SET IPCONVERGENCE
type: MMLCommand
name: SET IPCONVERGENCE（设置Bi口IPCONVERGENCE开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPCONVERGENCE
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- Bi口IP收敛功能
status: active
---

# SET IPCONVERGENCE（设置Bi口IPCONVERGENCE开关）

## 功能

![](设置Bi口IPCONVERGENCE开关（SET IPCONVERGENCE）_36016493.assets/notice_3.0-zh-cn_2.png)

属于高危命令，如果操作不当会导致话单业务严重受损，执行前请务必联系华为技术支持。

**适用NF：NCG**

该命令用于设置Bi口IP收敛功能。允许将多个RU上的话单汇聚到一个RU上，以此来解决扩容场景下计费中心需要多次适配的情况。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 该命令执行后，需在“话单存储(CDRSTOR)”命令的“最终话单文件名命名规则”中增加“增加模块名信息(%a或%A)”或“增加模块号信息(%B)”，防止话单汇聚时被覆盖。
- Bi收敛开关打开后，配置话单备份任务或话单分发PUSH任务前，需在每一个RUID上配置Omi或Bi&Omi的IP地址。
- 该命令最大记录数为1。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| IPCONVERGENCESWITCH |
| --- |
| OFF |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPCONVERGENCESWITCH | Bi口IPCONVERGENCE 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Bi口IPCONVERGENCE开关状态。数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPCONVERGENCE]] · Bi口IPCONVERGENCE开关状态（IPCONVERGENCE）

## 使用实例

设置Bi口IPCONVERGENCE开关状态为开启：

```
SET IPCONVERGENCE: IPCONVERGENCESWITCH=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Bi口IPCONVERGENCE开关（SET-IPCONVERGENCE）_36016493.md`
