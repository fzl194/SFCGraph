---
id: UNC@20.15.2@MMLCommand@SET GLBCDRFLDTEMP
type: MMLCommand
name: SET GLBCDRFLDTEMP（设置全局话单模板）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GLBCDRFLDTEMP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 话单字段控制
- 全局话单字段模板
status: active
---

# SET GLBCDRFLDTEMP（设置全局话单模板）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令是用来为全局绑定话单字段模板。

使用该命令可以为不同种类的话单类型绑定不同的话单字段模板（CDRFIELDTEMP）。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 设置全局计费属性，执行SET GLBCDRFLDTEMP命令前，需要执行ADD CDRFIELDTEMP添加话单字段模板。
- 输入空格表示解除全局话单字段模板的绑定关系。
- 全局绑定的话单字段优先级较低，如果APN下没有绑定某类型的话单字段模板时，才会使用全局绑定的该话单类型的话单字段模板，如果全局也没有绑定该类型的话单字段时，会使用默认配置。
- 此命令对新激活用户立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GCDRTEMPLATE | G-CDR话单字段模板名 | 可选必选说明：可选参数<br>参数含义：指定模板名称，设置G-CDR话单字段模板。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：该参数使用ADD CDRFIELDTEMP命令配置生成。 |
| PGWCDRTEMPLATE | PGW-CDR话单字段模板名 | 可选必选说明：可选参数<br>参数含义：指定模板名称，设置PGW-CDR话单字段模板。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：该参数使用ADD CDRFIELDTEMP命令配置生成。 |
| SGWCDRTEMPLATE | SGW-CDR话单字段模板名 | 可选必选说明：可选参数<br>参数含义：指定模板名称，设置SGW-CDR话单字段模板。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：该参数使用ADD CDRFIELDTEMP命令配置生成。 |

## 操作的配置对象

- [全局话单模板（GLBCDRFLDTEMP）](configobject/UNC/20.15.2/GLBCDRFLDTEMP.md)

## 使用实例

假如运营商想要配置全局绑定话单字段模板，G-CDR话单字段模板名为gcdr，PGW-CDR话单字段模板名为pgwcdr，SGW-CDR话单字段模板名为sgwcdr，命令为：

```
SET GLBCDRFLDTEMP:GCDRTEMPLATE="gcdr",PGWCDRTEMPLATE="pgwcdr",SGWCDRTEMPLATE="sgwcdr";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置全局话单模板（SET-GLBCDRFLDTEMP）_09896895.md`
