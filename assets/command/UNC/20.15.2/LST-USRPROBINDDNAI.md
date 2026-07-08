---
id: UNC@20.15.2@MMLCommand@LST USRPROBINDDNAI
type: MMLCommand
name: LST USRPROBINDDNAI（查询用户模板关联的DNAI）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRPROBINDDNAI
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板DNAI绑定
status: active
---

# LST USRPROBINDDNAI（查询用户模板关联的DNAI）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询用户模板关联的DNAI。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRPRONAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数通过ADD USERPROFILE命令配置生成。 |
| DNAI | 数据网络访问标识符 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识符。该参数的数据规划上需要和PNFDNAI命令中的“数据网络访问标识”参数保持一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户模板关联的DNAI（USRPROBINDDNAI）](configobject/UNC/20.15.2/USRPROBINDDNAI.md)

## 使用实例

查询指定用户模板关联的所有DNAI。 2. 查询指定DNAI关联的所有用户模板。

```
LST USRPROBINDDNAI: USRPRONAME="userprofile1";
RETCODE = 0  操作成功

结果如下
--------
       DNAI  =  huawei1.com
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户模板关联的DNAI（LST-USRPROBINDDNAI）_81530800.md`
