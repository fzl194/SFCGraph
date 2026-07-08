---
id: UNC@20.15.2@MMLCommand@LST CHGHOLI
type: MMLCommand
name: LST CHGHOLI（查询节假日配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGHOLI
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费节假日配置
status: active
---

# LST CHGHOLI（查询节假日配置）

## 功能

**适用网元：SGSN**

该命令用于查询节假日相关配置。节假日配置与费率时段配置（ [**ADD CHGTARI**](../计费费率时段配置/增加费率时段配置(ADD CHGTARI)_26305208.md) ）相结合，实现灵活的费率时段控制。

## 注意事项

如果有输入参数，则显示与输入参数均匹配的节假日记录；如果没有输入参数，则显示所有节假日记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CC | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定节假日是对普通计费属性用户、预付费计费属性用户、包月制计费属性用户还是对实时计费属性用户有效。<br>取值范围：<br>- “NORMAL(普通计费)”<br>- “PREPAID(预付费)”<br>- “FLATRATE(包月制)”<br>- “HOTBILLING(实时计费)”<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGHOLI]] · 节假日配置（CHGHOLI）

## 使用实例

1. 查询预付费计费属性节假日配置信息，配置格式为：
  LST CHGHOLI: CC=PREPAID;
  ```
  %%LST CHGHOLI: CC=PREPAID;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   年      月      日      计费属性

   2009    1       2       预付费
   2009    4       5       预付费   
   2009    9       20      预付费  
  (结果个数 = 3)

  ---    END
  ```
2. 查询所有的节假日配置记录，配置格式为：
  LST CHGHOLI:;
  ```
  %%LST CHGHOLI:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   年      月      日      计费属性

   2009    1       2       预付费
   2009    4       5       预付费
   2009    7       4       实时计费
   2009    8       12      普通计费
   2009    9       10      包月制
   2009    9       20      预付费     
  (结果个数 = 6)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGHOLI.md`
