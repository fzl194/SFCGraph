---
id: UNC@20.15.2@MMLCommand@LST RURESTHRESHOLD
type: MMLCommand
name: LST RURESTHRESHOLD（查询RU资源过载和去过载阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RURESTHRESHOLD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# LST RURESTHRESHOLD（查询RU资源过载和去过载阈值）

## 功能

该命令用来查看不同RU类型的资源过载和去过载阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUTYPE | RU类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：请使用<br>[**LST RESINSTANCETYPE**](查询资源实例类型（LST RESINSTANCETYPE）_59103378.md)<br>命令查询存在的资源单元类型。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [RU资源过载和去过载阈值（RURESTHRESHOLD）](configobject/UNC/20.15.2/RURESTHRESHOLD.md)

## 使用实例

查询VNODE_CSLB_VNFC_OMU类型的资源过载和去过载阈值：

```
LST RURESTHRESHOLD
:RUTYPE="VNODE_CSLB_VNFC_OMU"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
                                  RU类型  =  VNODE_CSLB_VNFC_OMU
 CPU使用率过载次要级别告警的恢复阈值（%） =  50
 CPU使用率过载次要级别告警的上报阈值（%） =  60
 CPU使用率过载重要级别告警的恢复阈值（%） =  75
 CPU使用率过载重要级别告警的上报阈值（%） =  80
 CPU使用率过载紧急级别告警的恢复阈值（%） =  85
 CPU使用率过载紧急级别告警的上报阈值（%） =  95
内存使用率过载次要级别告警的恢复阈值（%） =  50
内存使用率过载次要级别告警的上报阈值（%） =  60
内存使用率过载重要级别告警的恢复阈值（%） =  75
内存使用率过载重要级别告警的上报阈值（%） =  80
内存使用率过载紧急级别告警的恢复阈值（%） =  85
内存使用率过载紧急级别告警的上报阈值（%） =  95
(结果个数 = 1)
 ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RU资源过载和去过载阈值（LST-RURESTHRESHOLD）_56175397.md`
