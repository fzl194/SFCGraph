---
id: UDG@20.15.2@MMLCommand@DSP DEVATTRNOTIFY
type: MMLCommand
name: DSP DEVATTRNOTIFY（显示属性变更通知消息记录）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DEVATTRNOTIFY
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

# DSP DEVATTRNOTIFY（显示属性变更通知消息记录）

## 功能

该命令用于显示资源单元上指定组件的设备对象的属性变更通知消息记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPTYPE | 组件类型 | 可选必选说明：必选参数<br>参数含义：该参数表示组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEVMA：DEVMA组件，该组件用于收集本资源单元设备属性、运行状态和设备事件数据上报给总控模块，同时执行来自总控模块的各种设备操作。<br>- LDEVM：LDEVM组件，该组件用于给APP提供设备属性订阅功能。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEVATTRNOTIFY]] · 属性变更通知消息记录（DEVATTRNOTIFY）

## 使用实例

显示资源单元上指定组件的设备对象的属性变更通知消息记录：

```
DSP DEVATTRNOTIFY:COMPTYPE=LDEVM,RUNAME="CSDB_OM_RU_0001"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
发送时间                   发送到对端的PID    对象设备ID    属性ID    属性值                                  属性值长度 

2016/06/16 15:41:43.681    0x7A000E           0x17          0x13      01 00 00 00                             4          
2016/06/16 15:41:43.681    0x7A000E           0x17          0x2C      00 50 56 BE F0 65                       6          
2016/06/16 15:41:43.681    0x7A000E           0x17          0x2D      C0 BD F0 FF 3F 42 0F 00                 8          
2016/06/16 15:41:43.681    0x7A000E           0x17          0x127     00 00 00 00                             4                  
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示属性变更通知消息记录（DSP-DEVATTRNOTIFY）_59103965.md`
