---
id: UNC@20.15.2@MMLCommand@LST ROAMTYPEBINDUP
type: MMLCommand
name: LST ROAMTYPEBINDUP（查询UPF与用户漫游类型的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROAMTYPEBINDUP
command_category: 查询类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF绑定用户漫游属性
status: active
---

# LST ROAMTYPEBINDUP（查询UPF与用户漫游类型的绑定关系）

## 功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于查询UPF与用户漫游类型的绑定关系，对非ULCL场景生效。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROAMINGTYPE | 用户漫游类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户漫游类型。<br>数据来源：全网规划<br>取值范围：<br>- “INBOUND（漫入）”：对于漫入用户，使用绑定UPF过滤接入UPF列表。<br>- “OUTBOUND（漫出）”：对于漫出用户，使用绑定UPF过滤主锚点UPF列表。<br>默认值：无<br>配置原则：无 |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMTYPEBINDUP]] · UPF与用户漫游类型的绑定关系（ROAMTYPEBINDUP）

## 使用实例

显示UPF与用户漫游类型的绑定关系： LST ROAMTYPEBINDUP:;

```
%%LST ROAMTYPEBINDUP:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
用户漫游类型         UPF实例名称     

漫入                 UPF1
漫出                 UPF2
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ROAMTYPEBINDUP.md`
