---
id: UNC@20.15.2@MMLCommand@DSP SDRPOLICYINFO
type: MMLCommand
name: DSP SDRPOLICYINFO（显示SDRC中的策略版本信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDRPOLICYINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRPOLICYINFO（显示SDRC中的策略版本信息）

## 功能

该命令用于查询SDRC中的策略版本信息，包括版本号、Checksum、更新时间信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略类型。<br>数据来源：本端规划<br>取值范围：<br>- AppRoute（AppRoute）<br>- Topic（Topic）<br>- VpnIp（VpnIp）<br>- Token（Token）<br>- KeyMatch（KeyMatch）<br>- Service（Service）<br>- NextHop（NextHop）<br>- LbPolicy（LbPolicy）<br>- Vpn（Vpn）<br>- LbTopo（LbTopo）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDRPOLICYINFO]] · SDRC中的策略版本信息（SDRPOLICYINFO）

## 使用实例

查询SDRC中的策略版本信息：

```
%%DSP SDRPOLICYINFO: PLCYTYPE=Token;%%
RETCODE = 0  操作成功

结果如下
--------
策略         版本号  Checksum  更新时间
Token:1034   1       1         2022-05-16 15:04:05
Token:129    2       2         2022-05-16 14:04:05
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SDRPOLICYINFO.md`
