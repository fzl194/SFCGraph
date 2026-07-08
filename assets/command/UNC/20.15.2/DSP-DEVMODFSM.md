---
id: UNC@20.15.2@MMLCommand@DSP DEVMODFSM
type: MMLCommand
name: DSP DEVMODFSM（显示模块状态机信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DEVMODFSM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 设备管理
status: active
---

# DSP DEVMODFSM（显示模块状态机信息）

## 功能

该命令用于显示资源单元上指定组件的模块状态机信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| COMPTYPE | 组件类型 | 可选必选说明：必选参数<br>参数含义：该参数表示组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEVMA：DEVMA组件，该组件用于收集本资源单元设备属性、运行状态和设备事件数据上报给总控模块，同时执行来自总控模块的各种设备操作。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEVMODFSM]] · 模块状态机信息（DEVMODFSM）

## 使用实例

显示资源单元上指定组件的模块状态机信息：

```
DSP DEVMODFSM:RUNAME="CSDB_OM_RU_0001",COMPTYPE=DEVMA
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
       模块ID  =  0x2
     模块类型  =  0x3
         位置  =  0x1FFFF
模块状态迁移1  =  3 (-1)->4  15-15:43:43.734    
模块状态迁移2  =  2 (-1)->9  15-15:43:32.746    
模块状态迁移3  =  0 (0 )->0  00-00:00:00.000    
模块状态迁移4  =  0 (0 )->0  00-00:00:00.000    
模块状态迁移5  =  0 (0 )->0  00-00:00:00.000    
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DEVMODFSM.md`
