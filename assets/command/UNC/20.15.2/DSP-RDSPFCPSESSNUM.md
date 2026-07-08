---
id: UNC@20.15.2@MMLCommand@DSP RDSPFCPSESSNUM
type: MMLCommand
name: DSP RDSPFCPSESSNUM（显示RADIUS中转UPF的PFCP会话数目）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RDSPFCPSESSNUM
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
- RADIUS管理
- RADIUS维护
- RADIUS中转UPF会话信息
status: active
---

# DSP RDSPFCPSESSNUM（显示RADIUS中转UPF的PFCP会话数目）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于显示RADIUS中转UPF，UPC创建的会话数目。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（全部）<br>- UPFID（UP实例标识）<br>默认值：无<br>配置原则：无 |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"UPFID"时为条件必选参数。<br>参数含义：该参数用于指示UPF实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSPFCPSESSNUM]] · RADIUS中转UPF的PFCP会话数目（RDSPFCPSESSNUM）

## 使用实例

查询所有RADIUS中转UPF的会话数量。 DSP RDSPFCPSESSNUM: QUERYTYPE=ALL;

```
%%DSP RDSPFCPSESSNUM: QUERYTYPE=ALL;%%
RETCODE = 0  操作成功。

结果如下
------------------------
RADIUS中转UPF的PFCP会话数目  =  4
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示RADIUS中转UPF的PFCP会话数目（DSP-RDSPFCPSESSNUM）_35232166.md`
