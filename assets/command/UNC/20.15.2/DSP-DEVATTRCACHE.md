---
id: UNC@20.15.2@MMLCommand@DSP DEVATTRCACHE
type: MMLCommand
name: DSP DEVATTRCACHE（显示属性值信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DEVATTRCACHE
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

# DSP DEVATTRCACHE（显示属性值信息）

## 功能

该命令用于显示资源单元上指定组件的设备属性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPTYPE | 组件类型 | 可选必选说明：必选参数<br>参数含义：该参数表示组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LDEVM：LDEVM组件，该组件用于给APP提供设备属性订阅功能。<br>默认值：无 |
| DEVID | 设备ID | 可选必选说明：可选参数<br>参数含义：该参数表示设备ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| ATTRID | 属性ID | 可选必选说明：可选参数<br>参数含义：该参数表示属性ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DEVATTRCACHE]] · 属性值信息（DEVATTRCACHE）

## 使用实例

- 显示资源单元上指定组件的所有属性信息：
  ```
  DSP DEVATTRCACHE:COMPTYPE=LDEVM
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
  设备ID    属性ID    属性长度    超时次数    属性源PID     同步状态    属性值                               
  
  0x4       0x13      4           0           0x1           SYN         01 00 00 00  
  0x1C      0x2D      8           0           0x40          SYN         00 E4 0B 54 02 00 00 00              
  0x1D      0x2D      8           0           0x40          SYN         00 E4 0B 54 02 00 00 00              
  0x1E      0x2D      8           0           0x40          SYN         00 E4 0B 54 02 00 00 00              
  0x1F      0x2D      8           0           0x40          SYN         00 E4 0B 54 02 00 00 00 
  (结果个数 = 4)
  ---    END
  ```
- 显示资源单元上指定组件的指定设备对象的所有属性信息：
  ```
  DSP DEVATTRCACHE:COMPTYPE=LDEVM,DEVID="4"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
     设备ID  =  0x4
     属性ID  =  0x29
   属性长度  =  4
   超时次数  =  0
  属性源PID  =  0x1
   同步状态  =  SYN
     属性值  =  01 00 00 00
  (结果个数 = 1)
  ---    END
  ```
- 显示资源单元上指定组件的指定设备对象的某一个设备属性信息：
  ```
  DSP DEVATTRCACHE:COMPTYPE=LDEVM,DEVID="4",ATTRID="29"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
     设备ID  =  0x4
     属性ID  =  0x29
   属性长度  =  4
   超时次数  =  0
  属性源PID  =  0x1
   同步状态  =  SYN
     属性值  =  01 00 00 00
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DEVATTRCACHE.md`
