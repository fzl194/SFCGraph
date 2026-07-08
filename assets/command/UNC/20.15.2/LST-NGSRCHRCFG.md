---
id: UNC@20.15.2@MMLCommand@LST NGSRCHRCFG
type: MMLCommand
name: LST NGSRCHRCFG（查询AMF小范围CHR上报规则配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGSRCHRCFG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- CHR管理
- NG接入小范围CHR配置
status: active
---

# LST NGSRCHRCFG（查询AMF小范围CHR上报规则配置）

## 功能

**适用NF：AMF**

该命令用于查询AMF小范围CHR上报规则配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置小范围CHR的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- SPECIFIC_IMSI（指定用户IMSI）<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件可选参数。<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGSRCHRCFG]] · AMF小范围CHR上报规则配置（NGSRCHRCFG）

## 使用实例

- 查询IMSI前缀为12303000100的小范围CHR上报规则配置，执行如下命令：
  ```
  %%LST NGSRCHRCFG: SUBRANGE=SPECIFIC_IMSI, IMSIPRE="12303000100";%%
  RETCODE = 0  操作成功

  结果如下
  --------
          用户范围  =  指定用户IMSI
          IMSI前缀  =  12303000100
  流程控制模板索引  =  0
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中AMF小范围CHR上报的所有规则配置，执行如下命令：
  ```
  %%LST NGSRCHRCFG:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  用户范围      IMSI前缀     流程控制模板索引

  指定用户IMSI  12303000100  0
  指定用户IMSI  12303000101  1
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF小范围CHR上报规则配置（LST-NGSRCHRCFG）_58840351.md`
