---
id: UNC@20.15.2@MMLCommand@LST NGAREARESELPLCY
type: MMLCommand
name: LST NGAREARESELPLCY（查询AMF区域重选控制策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGAREARESELPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF区域重选策略
status: active
---

# LST NGAREARESELPLCY（查询AMF区域重选控制策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF区域重选功能控制策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREARANGE | 区域范围 | 可选必选说明：可选参数<br>参数含义：该参数用于设置指定区域重路由功能的区域范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_AREA（所有区域）”：所有区域<br>- “AREA_CODE（指定区域编码）”：指定区域编码<br>默认值：无<br>配置原则：<br>“所有区域”类型建议只在园区使用，避免误配置导致非园区用户业务受影响。 |
| RESELAREACODE | AMF重选功能区域编码 | 可选必选说明：该参数在"AREARANGE"配置为"AREA_CODE"时为条件可选参数。<br>参数含义：该参数用于指定应用AMF重选功能的某个区域。该参数已经通过ADD RESELAREACODE命令中的RESELAREACODE参数配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该区域编码必须先通过ADD RESELAREACODE进行添加；而区域内的跟踪区列表则通过ADD RESELAREAMEM进行添加。<br>默认值：无<br>配置原则：无 |
| CTRLOBJECT | 控制对象 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用指定区域重路由功能的用户的识别对象。<br>数据来源：全网规划<br>取值范围：<br>- “USER_GROUP（用户群）”：用户群<br>- “SUB_NS（签约切片）”：签约切片<br>- “NO_SUB（无签约信息）”：无签约信息<br>默认值：无<br>配置原则：<br>“无签约信息”类型建议只在园区使用，避免误配置导致非园区用户业务受影响。 |
| SUBGRPID | 用户群组标识 | 可选必选说明：该参数在"CTRLOBJECT"配置为"USER_GROUP"时为条件可选参数。<br>参数含义：该参数用于指定应用AMF重选功能的用户群组。该参数已经通过ADD NGUSRGRP命令中的USRGRPID参数配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。该用户群组标识通过ADD NGUSRGRP进行添加；群组内的用户标识列表通过ADD NGUSRGRPMEM进行添加。<br>默认值：无<br>配置原则：<br>当针对指定的区域，有多个用户（号段）需要进行AMF重选时，建议通过本参数指定用户范围。<br>该值若不设置，默认值为4294967295。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"CTRLOBJECT"配置为"SUB_NS"时为条件可选参数。<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>该值若不设置，默认值为65535。 |
| SD | 切片细分标识 | 可选必选说明：该参数在"CTRLOBJECT"配置为"SUB_NS"时为条件可选参数。<br>参数含义：该参数表示根据网络切片所提供的服务特点、所服务的对象差异，对某种网络切片的进一步细分。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>该值若不设置，默认值为FFFFFF。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGAREARESELPLCY]] · AMF区域重选控制策略（NGAREARESELPLCY）

## 使用实例

- 查询区域编码为“ReSelZone”，用户群组标识“1”的AMF区域重选控制策略，执行如下命令：
  ```
  %%LST NGAREARESELPLCY: AREARANGE=AREA_CODE, RESELAREACODE="ReSelZone",  CTRLOBJECT=USER_GROUP, SUBGRPID=1;%%
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
             区域范围  =  指定区域编码
  AMF重选功能区域编码  =  ReSelZone
             控制对象  =  用户群
         用户群组标识  =  1
         切片业务类型  =  65535
         切片细分标识  =  FFFFFF
             控制模式  =  重路由
           目标AMFSET  =  111
  (结果个数 = 1)

  ---    END
  ```
- 查询当前系统的所有AMF区域重选控制策略，执行如下命令：
  ```
  %%LST NGAREARESELPLCY:;%%
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  区域范围      AMF重选功能区域编码  控制对象    用户群组标识  切片业务类型  切片细分标识  控制模式  目标AMFSET  

  所有区域      NULL                 无签约信息  4294967295    65535         FFFFFF        重路由    111             
  指定区域编码  ReSelZone            用户群      1             65535         FFFFFF        重路由    111             
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF区域重选控制策略（LST-NGAREARESELPLCY）_70462549.md`
