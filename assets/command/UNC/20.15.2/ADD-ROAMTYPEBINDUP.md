---
id: UNC@20.15.2@MMLCommand@ADD ROAMTYPEBINDUP
type: MMLCommand
name: ADD ROAMTYPEBINDUP（增加UPF与用户漫游类型的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ROAMTYPEBINDUP
command_category: 配置类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF绑定用户漫游属性
status: active
---

# ADD ROAMTYPEBINDUP（增加UPF与用户漫游类型的绑定关系）

## 功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于增加UPF与用户漫游类型的绑定关系，对非ULCL场景生效。

## 注意事项

- 该命令执行后立即生效。

- 该配置只针对GGSN、SGW-C、PGW-C、VSMF、N16SMF形态生效。
- 该配置只适用于Home Routed漫游，不适用于Local Breakout漫游。
- 当只配置漫入UPF时，该配置只对过滤接入UPF列表生效；当只配置漫出UPF时，该配置只对过滤主锚点UPF列表选择生效。
- 该配置只有在UPSELECTFLAG的ROAMTYPEFLAG参数打开时生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROAMINGTYPE | 用户漫游类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户漫游类型。<br>数据来源：全网规划<br>取值范围：<br>- “INBOUND（漫入）”：对于漫入用户，使用绑定UPF过滤接入UPF列表。<br>- “OUTBOUND（漫出）”：对于漫出用户，使用绑定UPF过滤主锚点UPF列表。<br>默认值：无<br>配置原则：无 |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMTYPEBINDUP]] · UPF与用户漫游类型的绑定关系（ROAMTYPEBINDUP）

## 使用实例

当用户从国内移动到国外，并且漫游类型为Home Routed漫游时，如果希望用户能在指定UPF上建立会话，需新增拜访地UPF与用户漫游类型的绑定关系，其中用户漫游类型为INBOUND，UPF标识为“UPF1”；归属地UPF与用户漫游类型的绑定关系，其中用户漫游类型为OUTBOUND，UPF标识为“UPF2”：

```
ADD ROAMTYPEBINDUP: ROAMINGTYPE=INBOUND, NFINSTANCENAME="UPF1";
ADD ROAMTYPEBINDUP: ROAMINGTYPE=OUTBOUND, NFINSTANCENAME="UPF2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF与用户漫游类型的绑定关系（ADD-ROAMTYPEBINDUP）_51145562.md`
