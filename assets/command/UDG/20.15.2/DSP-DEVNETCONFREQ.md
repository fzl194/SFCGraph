---
id: UDG@20.15.2@MMLCommand@DSP DEVNETCONFREQ
type: MMLCommand
name: DSP DEVNETCONFREQ（显示NETCONF请求信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DEVNETCONFREQ
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

# DSP DEVNETCONFREQ（显示NETCONF请求信息）

## 功能

该命令用于显示NETCONF请求信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEVNETCONFREQ]] · NETCONF请求信息（DEVNETCONFREQ）

## 使用实例

显示NETCONF请求信息：

```
DSP DEVNETCONFREQ:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
VNFC ID    时间                       通道ID    操作码    结果 

0x0        2016/07/04 20:33:19.571    360448    0x0       0    
0x0        2016/07/04 20:33:19.889    360448    0x1       0    
0x0        2016/07/04 20:33:30.537    360448    0x0       0    
0x0        2016/07/04 20:33:30.887    360448    0x1       0    
0x0        2016/07/04 20:33:41.562    360448    0x0       0    
0x0        2016/07/04 20:33:41.894    360448    0x1       0       
(结果个数 = 6)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DEVNETCONFREQ.md`
