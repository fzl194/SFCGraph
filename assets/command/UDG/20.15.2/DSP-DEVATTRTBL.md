---
id: UDG@20.15.2@MMLCommand@DSP DEVATTRTBL
type: MMLCommand
name: DSP DEVATTRTBL（显示设备属性信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DEVATTRTBL
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

# DSP DEVATTRTBL（显示设备属性信息）

## 功能

该命令用于查询设备属性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPTYPE | 组件类型 | 可选必选说明：必选参数<br>参数含义：该参数表示组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEVMA：DEVMA组件，该组件用于收集本资源单元设备属性、运行状态和设备事件数据上报给总控模块，同时执行来自总控模块的各种设备操作。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| DEVID | 设备编号 | 可选必选说明：必选参数<br>参数含义：该参数表示设备编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEVATTRTBL]] · 设备属性信息（DEVATTRTBL）

## 使用实例

显示指定设备的属性信息：

```
DSP DEVATTRTBL:COMPTYPE=DEVMA,RUNAME="CSDB_OM_RU_0001",DEVID=5
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
设备编号    属性设备类型    属性ID   属性名称       数据类型    属性值       

5           0               1        devName        7           eth1                   
5           0               2        position       11          0x20001                
5           0               3        devType        11          0x26                   
5           0               4        hardType       11          0x10000102                                 
5           0               19       isAvailable    11          0x1                        
5           38              473      udevName       7           eth1                   
5           38              474      udevMac        17          00e0-fc23-3ccb         
5           38              476      drvName        7           0                      
5           38              478      phyiffup       11          0x1                                       
(结果个数 = 9)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示设备属性信息（DSP-DEVATTRTBL）_59103741.md`
