---
id: UDG@20.15.2@MMLCommand@DSP DEVATTRREV
type: MMLCommand
name: DSP DEVATTRREV（显示接收VNFC配置的属性信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DEVATTRREV
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

# DSP DEVATTRREV（显示接收VNFC配置的属性信息）

## 功能

该命令用于显示在VNFC上配置的属性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCID | VNFC ID | 可选必选说明：可选参数<br>参数含义：该参数表示VNFC的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DEVATTRREV]] · 接收VNFC配置的属性信息（DEVATTRREV）

## 使用实例

显示在指定VNFC上配置的所有属性值信息：

```
DSP DEVATTRREV:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
时间                       VNFC ID    位置      设备类型    序列号    属性ID    属性长度    属性值                                 消息类型 

2016/05/03 19:37:40.368    0          131072    39          131073    45        8           00 CA 9A 3B 00 00 00 00                8            
2016/05/03 19:37:40.368    0          131073    38          196607    45        8           00 CA 9A 3B 00 00 00 00                8            
2016/05/03 19:37:40.368    0          65536     38          196607    370       12          FF FF FF FF 01 00 00 00 15 00 00 00    8            
2016/05/03 19:37:40.368    0          65536     39          131074    370       12          FF FF FF FF 01 00 00 00 15 00 00 00    8            
2016/05/03 19:37:40.368    0          65536     39          131072    370       12          FF FF FF FF 01 00 00 00 15 00 00 00    8            
2016/05/03 19:37:40.368    0          65536     39          131073    370       12          FF FF FF FF 01 00 00 00 15 00 00 00    8                                           
(结果个数 = 6)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DEVATTRREV.md`
