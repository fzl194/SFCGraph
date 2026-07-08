---
id: UDG@20.15.2@MMLCommand@LST MEASRST
type: MMLCommand
name: LST MEASRST（查询测量结果文件）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MEASRST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# LST MEASRST（查询测量结果文件）

## 功能

该命令用于查询网元上的测量结果文件状态。

> **说明**
> 执行该MML前， UDG 需要完成MAE对接。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| SDT | 开始时间 | 可选必选说明：可选参数。<br>参数含义：查询起始时间。<br>取值范围：年月日时分秒，规则为YYYY/MM/DD HH:MM:SS。<br>默认值：无。<br>配置原则：若不输入，则表示该参数不作为查询的限制条件。 |
| EDT | 结束时间 | 可选必选说明：可选参数。<br>参数含义：查询结束时间。<br>取值范围：年月日时分秒，规则为YYYY/MM/DD HH:MM:SS。<br>默认值：无。<br>配置原则：若不输入，则表示该参数不作为查询的限制条件。 |
| PRD | 周期 | 可选必选说明：可选参数。<br>参数含义：标识查询的周期。<br>取值范围：<br>- ALL(全部)<br>- FIVE(5分钟)<br>- FIFTEEN(15分钟)<br>- THIRTY(30分钟)<br>- SIXTY(1小时)<br>- ONE_DAY(一天)<br>默认值：ALL(全部)。<br>配置原则：若不输入，则表示查询所有周期的测量结果文件。 |
| ISULD | 是否已上报 | 可选必选说明：可选参数。<br>参数含义：测量结果文件是否已上报网管。<br>取值范围：<br>- NO_UPLOAD(未上报)<br>- UPLOADED(已上报)<br>- ALL(全部)<br>默认值：NO_UPLOAD(未上报)。<br>配置原则：若不输入，则表示查询未上报网管的测量结果文件。 |
| EMS | 网管类型 | 可选必选说明：必选参数。<br>参数含义：网管类型。<br>取值范围：1~65535。<br>默认值：无。<br>配置原则：联系相应的网管运维人员获取网管类型。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MEASRST]] · 测量结果文件（MEASRST）

## 使用实例

1. 查询网元测量结果文件状态：
  ```
  %%LST MEASRST: NEID=10, ISULD=NO_UPLOAD, EMS=1;%%
  RETCODE = 0  操作成功

  测量结果列表
  ------------
  文件名                                                            创建时间             

  A20200630.0025+0800-0030+0800_jly01_cscf-v.4_EMS-SHORTPERIOD.mrf  2020-07-01 23:04:47  
  A20200630.0030+0800-0035+0800_jly01_cscf-v.4_EMS-SHORTPERIOD.mrf  2020-07-01 23:04:47  
  A20200630.0035+0800-0040+0800_jly01_cscf-v.4_EMS-SHORTPERIOD.mrf  2020-07-01 23:04:47  
  A20200630.0030+0800-0045+0800_jly01_cscf-v.4_EMS-NORMAL.mrf       2020-07-01 23:04:47  
  A20200630.0040+0800-0045+0800_jly01_cscf-v.4_EMS-SHORTPERIOD.mrf  2020-07-01 23:04:47  
  A20200630.0045+0800-0050+0800_jly01_cscf-v.4_EMS-SHORTPERIOD.mrf  2020-07-01 23:04:47  
  A20200701.2240+0800-2245+0800_jly01_cscf-v.4_EMS-SHORTPERIOD.mrf  2020-07-01 23:04:47  
  A20200701.2250+0800-2255+0800_jly01_cscf-v.4_EMS-SHORTPERIOD.mrf  2020-07-01 23:04:47  
  (结果个数 = 8)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MEASRST.md`
