---
id: UNC@20.15.2@MMLCommand@DSP UPLOCKINFO
type: MMLCommand
name: DSP UPLOCKINFO（显示UPF上报的锁定信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UPLOCKINFO
command_category: 查询类
applicable_nf:
- SMF
- GGSN
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF锁定信息
status: active
---

# DSP UPLOCKINFO（显示UPF上报的锁定信息）

## 功能

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于查询UPF上报的锁定信息，包括锁定状态和APN锁定列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（所有）<br>- NFDESCNAME（UPF描述名称）<br>- NFINSTANCENAME（UPF实例名称）<br>默认值：ALL<br>配置原则：无 |
| NFDESCNAME | UPF描述名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFDESCNAME"时为条件必选参数。<br>参数含义：该参数用于指定UPF的描述名称。当需要查询指定UPF的锁定信息时，可以指定该参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF描述名称”参数取值保持一致。 |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFINSTANCENAME"时为条件必选参数。<br>参数含义：该参数用于指定UPF的实例名称。当需要查询指定UPF的锁定信息时，可以指定该参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UPF上报的锁定信息（UPLOCKINFO）](configobject/UNC/20.15.2/UPLOCKINFO.md)

## 使用实例

查询所有UPF在U面的锁定信息。DSP UPLOCKINFO:QUERYTYPE=ALL;

```
%%DSP UPLOCKINFO: QUERYTYPE=ALL;%%
RETCODE = 0  操作成功。

结果如下
--------
UPF描述名称						UPF实例名称      		UPF锁定状态             APN锁定列表

UPF-beijingRegion-beijing-toB-b001			upf_instance_1			锁定                    huawei.com
UPF-beijingRegion-beijing-toB-b002			upf_instance_2			未锁定	            	
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UPF上报的锁定信息（DSP-UPLOCKINFO）_43898229.md`
