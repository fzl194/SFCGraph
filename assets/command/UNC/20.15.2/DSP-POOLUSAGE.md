---
id: UNC@20.15.2@MMLCommand@DSP POOLUSAGE
type: MMLCommand
name: DSP POOLUSAGE（显示地址池使用信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: POOLUSAGE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池使用信息
status: active
---

# DSP POOLUSAGE（显示地址池使用信息）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于显示本地地址池使用信息。

## 注意事项

当前版本暂时不支持基于APN名称、UPF实例标识查询本地地址池使用信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- POOL（地址池）<br>- APN（APN名称）<br>- UPFID（UPF实例名称）<br>默认值：POOL<br>配置原则：无 |
| POOLNAME | 地址池名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"POOL"时为条件必选参数。<br>参数含义：该参数用于指定已配的本地地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| APN | APN名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"APN"时为条件必选参数。<br>参数含义：该参数用于指定APN/DNN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| UPFID | UPF实例标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"UPFID"时为条件必选参数。<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>该参数使用ADD UPNODE命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/POOLUSAGE]] · 地址池使用信息（POOLUSAGE）

## 使用实例

显示地址池名称为testpool的地址池使用率信息： DSP POOLUSAGE:POOLNAME="testpool";

```
%%DSP POOLUSAGE:POOLNAME="testpool";%%
RETCODE = 0  操作成功

结果如下
-------------------------
    地址池名称  =  testpool
  等待释放IP数  =  0
      地址段数  =  1
      地址总数  =  31
    地址使用数  =  0
    无效地址数  =  0
    锁定地址数  =  0
地址使用率 (%)  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-POOLUSAGE.md`
