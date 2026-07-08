---
id: UNC@20.15.2@MMLCommand@DSP DEVBOOTPRES
type: MMLCommand
name: DSP DEVBOOTPRES（显示BOOTP服务器本地资源信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DEVBOOTPRES
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

# DSP DEVBOOTPRES（显示BOOTP服务器本地资源信息）

## 功能

该命令用于显示BOOTP服务器本地资源信息。用户可使用该命令查询BOOTP服务器本地资源的MAC地址、端口号等信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEVBOOTPRES]] · BOOTP服务器本地资源信息（DEVBOOTPRES）

## 使用实例

显示BOOTP服务器本地资源信息：

```
DSP DEVBOOTPRES:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
RU编号    设备ID    硬件类型      网络IP     网络MAC1          网络MAC2          BoardInf配置下发时间   BOOTP服务器端口号   BOOTP客户端端口号
                                      
1         0x2       0x2           X.X.X.X    00E0-FCXX-XXXX    00E0-FCXX-XXXX    2017-01-18 15:57:02    1067                1068
2         0xA       0x2           X.X.X.X    00E0-FCXX-XXXX    00E0-FCXX-XXXX    2017-01-18 15:57:02    1067                1068
64        0x12      0x10000011    X.X.X.X    00E0-FCXX-XXXX    00E0-FCXX-XXXX    2017-01-18 15:57:02    1067                1068
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示BOOTP服务器本地资源信息（DSP-DEVBOOTPRES）_59103739.md`
