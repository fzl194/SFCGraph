---
id: UNC@20.15.2@MMLCommand@DSP LOCALRECOVERY
type: MMLCommand
name: DSP LOCALRECOVERY（显示本端Recovery值及系统重启时间）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LOCALRECOVERY
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- Recovery管理
status: active
---

# DSP LOCALRECOVERY（显示本端Recovery值及系统重启时间）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于查询本端Recovery值及系统重启时间。

## 注意事项

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP RECOVERY / MOD RECOVERY配置。
- 本端Recovery值仅在公共软参DWORD4 BIT16设置为1时增加。
- 系统重启时间是否刷新由DWORD4 BIT15软参控制。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALRECOVERY]] · 本端Recovery值及系统重启时间（LOCALRECOVERY）

## 使用实例

查询本端Recovery值及系统重启时间：DSP LOCALRECOVERY:;

```
%%DSP LOCALRECOVERY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  本端Recovery值  =  0
      系统重启时间  =  2021-03-04 00:00:00
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示本端Recovery值及系统重启时间（DSP-LOCALRECOVERY）_88248944.md`
