---
id: UNC@20.15.2@MMLCommand@LST MONVPN
type: MMLCommand
name: LST MONVPN（查询监控VPN实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MONVPN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST MONVPN（查询监控VPN实例）

## 功能

该命令用于查询监控VPN实例。

## 注意事项

该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置容灾组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |
| VPNGRPID | VPN组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MONVPN]] · 监控VPN实例（MONVPN）

## 使用实例

查询监控VPN实例:

```
%%LST MONVPN:DRGROUPID=1,VPNGRPID=1;%%
RETCODE = 0  操作成功

结果如下
--------
 容灾组标识 = 1
  VPN组标识 = 1
VPN实例名称 = 1
是否联动快速隔离 = 否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MONVPN.md`
