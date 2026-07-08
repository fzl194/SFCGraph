---
id: UNC@20.15.2@MMLCommand@LST CHGDCHAR
type: MMLCommand
name: LST CHGDCHAR（查询缺省计费属性参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGDCHAR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 缺省计费属性参数配置
status: active
---

# LST CHGDCHAR（查询缺省计费属性参数）

## 功能

**适用网元：SGSN**

该命令用于查询缺省计费属性参数配置表的相关配置。缺省计费属性是指当外网用户签约的HLR没有为外网用户指定计费属性时，SGSN将会按照该外网用户的MCC和MNC对应的缺省计费方式对该外网用户实施计费。

## 注意事项

如果有输入参数，则显示与输入参数相匹配的缺省计费属性参数配置信息；如果没有输入参数，则显示所有的缺省计费属性参数配置信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ST | 用户类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定缺省计费属性适用于漫游用户还是拜访用户。<br>取值范围：<br>- “ROAMING(漫游用户)”：表示使用归属PLMN的GGSN的外网用户。<br>- “VISITING(拜访用户)”：表示使用本PLMN的GGSN的外网用户。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGDCHAR]] · 缺省计费属性参数（CHGDCHAR）

## 使用实例

1. 查询拜访用户的缺省计费属性参数配置信息，配置格式为：
  LST CHGDCHAR: ST=VISITING;
  ```
  %%LST CHGDCHAR: ST=VISITING;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   用户类型  移动国家码   移动网号  缺省计费属性

   拜访用户  123           000       普通计费
   拜访用户  123           01        普通计费
  (结果个数 = 2)
  ---    END
  ```
2. 查询所有的缺省计费属性参数配置信息，配置格式为：
  LST CHGDCHAR:;
  ```
  %%LST CHGDCHAR:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  ----------------------
   用户类型  移动国家码   移动网号  缺省计费属性

   漫游用户  123           00        普通计费
   漫游用户  123           01        普通计费
   拜访用户  123           000       普通计费
   拜访用户  123           01        普通计费
  (结果个数 = 4)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGDCHAR.md`
