---
id: UDG@20.15.2@MMLCommand@ADD EPRPDYN
type: MMLCommand
name: ADD EPRPDYN（添加EPRPDYN对象）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: EPRPDYN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 72
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- EPRPDYN性能统计对象
status: active
---

# ADD EPRPDYN（添加EPRPDYN对象）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于添加EPRPDYN对象，对象由对象名称，本端IP地址列表和对端网段列表组成。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为72。
- 在添加n3if或saif逻辑接口时，会自动添加接口类型为N3UPF、名称为EpRpDynN3Upf_Global的EPRP对象；在添加scif、paif或n9cif逻辑接口时，会自动添加接口类型为N9UPF、名称为EpRpDynN9Upf_Global的EPRP对象；在添加paif逻辑接口时，会自动添加接口类型为S5S8PGW、名称为EpRpDynS5S8Pgwu_Global的EPRP对象；在添加s11或saif逻辑接口时，会自动添加接口类型为S11USGW、名称为EpRpDynS11uSgw_Global的EPRP对象；在添加s5-s或scif逻辑接口时，会自动添加接口类型为S5S8SGW、名称为EpRpDynS5S8Sgwu_Global的EPRP对象；自动创建的对象不占用对应接口类型最大实例规格数，只占用总规格数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- S5S8PGW：接口类型为S5S8PGW，最大配置规格为12。<br>- S5S8SGW：接口类型为S5S8SGW，最大配置规格为12。<br>- N3UPF：接口类型为N3，最大配置规格为12。<br>- N9UPF：接口类型为N9，最大配置规格为12。<br>- S1USGW：接口类型为S1U，最大配置规格为12。<br>- S11USGW：接口类型为S11U，最大配置规格为12。<br>默认值：无<br>配置原则：无 |
| EPRPDYNNAME | 对象名称 | 可选必选说明：必选参数<br>参数含义：对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格以及特殊字符：“_”、“#”、“$”等。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [EPRPDYN对象（EPRPDYN）](configobject/UDG/20.15.2/EPRPDYN.md)

## 使用实例

添加接口类型为S5S8PGW对象名为pgw1的EPRPDYN对象：

```
ADD EPRPDYN:INTERFACETYPE=S5S8PGW,EPRPDYNNAME="pgw1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加EPRPDYN对象（ADD-EPRPDYN）_82837835.md`
