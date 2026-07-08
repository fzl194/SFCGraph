---
id: UDG@20.15.2@MMLCommand@DSP DEVATTRSND
type: MMLCommand
name: DSP DEVATTRSND（显示VNFC同步到VNFP的属性信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DEVATTRSND
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

# DSP DEVATTRSND（显示VNFC同步到VNFP的属性信息）

## 功能

该命令用于显示VNFC同步到VNFP的属性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCID | VNFC ID | 可选必选说明：可选参数<br>参数含义：该参数表示VNFC的ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DEVATTRSND]] · VNFC同步到VNFP的属性信息（DEVATTRSND）

## 使用实例

- 显示VNFC同步到VNFP的所有属性值信息：
  ```
  DSP DEVATTRSND:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
  发送时间                   返回码    响应时间                   通道ID     VNFC ID    消息类型    位置       设备类型    序列号    属性ID    属性长度    属性值                               

  2016/06/16 15:44:09.070    0x0       2016/06/16 15:44:09.077    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0xC5      7           E0 07 06 10 0F 2C 08                 
  2016/06/16 15:44:13.938    0x0       2016/06/16 15:44:13.945    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0x25      4           00 00 00 00                          
  2016/06/16 15:44:13.938    0x0       2016/06/16 15:44:13.945    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0xFB      12          FF FF FF FF 00 00 00 00 63 00 00 00  
  2016/06/16 15:44:14.038    0x0       2016/06/16 15:44:14.045    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0xFD      7           E0 07 06 10 0F 2C 0D                 
  2016/06/16 15:44:23.642    0x0       2016/06/16 15:44:23.648    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0x29      8           00 E4 0B 54 02 00 00 00              
  (结果个数 = 5)
  ---    END
  ```
- 显示指定VNFC同步到VNFP的所有属性值信息：
  ```
  DSP DEVATTRSND:VNFCID="2"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
  发送时间                   返回码    响应时间                   通道ID     VNFC ID    消息类型    位置       设备类型    序列号    属性ID    属性长度    属性值                               

  2016/06/16 15:44:09.070    0x0       2016/06/16 15:44:09.077    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0xC5      7           E0 07 06 10 0F 2C 08                 
  2016/06/16 15:44:13.938    0x0       2016/06/16 15:44:13.945    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0x25      4           00 00 00 00                          
  2016/06/16 15:44:13.938    0x0       2016/06/16 15:44:13.945    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0xFB      12          FF FF FF FF 00 00 00 00 63 00 00 00  
  2016/06/16 15:44:14.038    0x0       2016/06/16 15:44:14.045    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0xFD      7           E0 07 06 10 0F 2C 0D                 
  2016/06/16 15:44:23.642    0x0       2016/06/16 15:44:23.648    0xD8000    0x2        8           0x10000    0x26        0x1FFFF   0x29      8           00 E4 0B 54 02 00 00 00              
  (结果个数 = 5)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DEVATTRSND.md`
