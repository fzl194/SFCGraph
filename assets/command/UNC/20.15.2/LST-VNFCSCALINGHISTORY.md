---
id: UNC@20.15.2@MMLCommand@LST VNFCSCALINGHISTORY
type: MMLCommand
name: LST VNFCSCALINGHISTORY（查询基于VNFC的扩缩容历史信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VNFCSCALINGHISTORY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- scale功能管理
status: active
---

# LST VNFCSCALINGHISTORY（查询基于VNFC的扩缩容历史信息）

## 功能

该命令用来查看本地资源超过阈值触发、MANO下发命令触发或者命令行触发的扩缩容历史记录。

## 注意事项

本命令最多显示100条最近产生的扩缩容历史记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SHOWNUM | 查询数据条数 | 可选必选说明：可选参数。<br>参数含义：查询数据条数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100<br>默认值：无。 |
| BEGTM | 查询数据开始时间 | 可选必选说明：可选参数。<br>参数含义：查询数据开始时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是YYYY/MM/DD HH:MM:SS<br>默认值：无。 |
| ENDTM | 查询数据结束时间 | 可选必选说明：可选参数。<br>参数含义：查询数据结束时间。<br>数据来源：本端规划<br>取值范围：时间类型，输入格式是YYYY/MM/DD HH:MM:SS<br>默认值：无。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VNFCSCALINGHISTORY]] · 基于VNFC的扩缩容历史信息（VNFCSCALINGHISTORY）

## 使用实例

显示扩缩容历史记录：

LST VNFCSCALINGHISTORY: SERVICEINSTANCE="CSLB_VNFC_999" ;

```
%%/*394*/LST VNFCSCALINGHISTORY:
SERVICEINSTANCE="
CSLB_VNFC_999
"
;%%
RETCODE = 0  操作成功.

结果如下
--------
             扩缩容类型   =  扩容
     扩缩容触发场景类型   =  本地自动扩缩容 
         扩缩容开始时间   =  2015-12-18 11:34:28
         扩缩容结束时间   =  2015-12-18 11:36:29
         扩缩容RU的个数   =  1
         扩缩容执行结果   =  处理全部完成  
     扩缩容结果备注信息   =  网元CSLB。扩容成功。
 (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于VNFC的扩缩容历史信息(LST-VNFCSCALINGHISTORY)_29626920.md`
