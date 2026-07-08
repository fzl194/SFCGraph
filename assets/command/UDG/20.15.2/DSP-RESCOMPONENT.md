---
id: UDG@20.15.2@MMLCommand@DSP RESCOMPONENT
type: MMLCommand
name: DSP RESCOMPONENT（显示组件信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESCOMPONENT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP RESCOMPONENT（显示组件信息）

## 功能

该命令用于显示组件信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- **QUERYBYPROCID**：根据进程ID查询组件信息。<br>- **QUERYBYCOMPCID**：根据组件ID查询组件信息。<br>默认值：<br>**QUERYBYPROCID** |
| PROCID | 进程ID | 可选必选说明：条件必选参数，该参数在“QUERYTYPE”配置为“QUERYBYPROCID”时为必选参数。<br>参数含义：该参数用于指定要查询组件所属进程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| COMPNAME | 组件名 | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“QUERYBYPROCID”时为可选参数。<br>参数含义：该参数用于指定要查询的组件名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无 |
| COMPSTATE | 状态 | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“QUERYBYPROCID”时为可选参数。<br>参数含义：组件的主备状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- **PRIMARY**：主用组件。<br>- **BACKUP**：备用组件。<br>- **FAILURE**：组件运行失败。<br>- **NOTBACKUP**：批备未完成状态。<br>- **NULL**：组件不存在。<br>- **INVALID**：角色未定。<br>- **COLDBACKUP**：冷备组件。<br>默认值：无 |
| COMPCID | 组件ID | 可选必选说明：条件必选参数，该参数在“QUERYTYPE”配置为“QUERYBYCOMPCID”时为必选参数。<br>参数含义：该参数用于指定要查询的组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [组件信息（RESCOMPONENT）](configobject/UDG/20.15.2/RESCOMPONENT.md)

## 使用实例

- 在VNFP侧查询进程1000上组件信息：
  ```
  DSP RESCOMPONENT:QUERYTYPE=QUERYBYPROCID,PROCID=1000;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  组件名    组件ID        逻辑ID       资源名称    进程ID    组件类型    版本号     状态    CPU使用率（%）    内存使用大小（KB）

  HTTPS     0x82D80015    0x2D8000C    OMU1        1000      0x2D8       1.2.103    主      0                 635
  HTTPC     0x82D70014    0x2D7000B    OMU1        1000      0x2D7       1.2.103    主      0                 633
  NETCONFC  0x81970013    0x197000A    OMU1        1000      0x197       1.2.103    主      0                 249
  APPCFG    0x80CF0011    0xCF0008     OMU1        1000      0xCF        1.2.103    主      0                 58
  NETCONF   0x80970012    0x970009     OMU1        1000      0x97        1.2.103    主      0                 5804
  SSHS      0x8093001B    0x930010     OMU1        1000      0x93        1.2.103    主      0                 1789
  SSHC      0x8092001A    0x92000F     OMU1        1000      0x92        1.2.103    主      0                 1166
  (结果个数 = 6)

  ---    END
  ```
- 在VNFP侧查询组件0x82D9002F的信息：
  ```
  DSP RESCOMPONENT:QUERYTYPE=QUERYBYCOMPCID,COMPCID="0x80970012";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
              组件名  =  NETCONFC
              组件ID  =  0x80970012
              逻辑ID  =  0x197000A
            资源名称  =  OMU1
              进程ID  =  1000
            组件类型  =  0x197
              版本号  =  1.2.103
                状态  =  主
      CPU使用率（%）  =  0
  内存使用大小（KB）  =  249
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示组件信息（DSP-RESCOMPONENT）_57993313.md`
