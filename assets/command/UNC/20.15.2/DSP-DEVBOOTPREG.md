---
id: UNC@20.15.2@MMLCommand@DSP DEVBOOTPREG
type: MMLCommand
name: DSP DEVBOOTPREG（显示BOOTP服务端的注册信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DEVBOOTPREG
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

# DSP DEVBOOTPREG（显示BOOTP服务端的注册信息）

## 功能

该命令用于显示BOOTP服务端的注册信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [BOOTP服务端的注册信息（DEVBOOTPREG）](configobject/UNC/20.15.2/DEVBOOTPREG.md)

## 使用实例

显示BOOTP服务端的注册信息：

```
DSP DEVBOOTPREG:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
RU编号    VNFM分配的资源编号    资源实例类型          请求MAC地址       请求源IP    请求目的IP    硬件类型      网元ID                      请求次数    上次返回码    端口名称    上次请求时间           上次回应时间     
                                
64        NE=34618142           VNODE_UGW_VNFC_SPU    00E0-FCXX-XXXX    X.X.X.X     X.X.X.X       0x10000011    RA2014112714373868696E35    5           0             eth0        2017-01-18 15:57:04    2017-01-18 15:57:04 
2         NE=34618143           VNODE_UGW_VNFC_OMU    00E0-FCXX-XXXX    X.X.X.X     X.X.X.X       0x2           RA2014112714373868696E35    2           0             eth0        2017-01-18 15:57:36    2017-01-18 15:57:36 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示BOOTP服务端的注册信息（DSP-DEVBOOTPREG）_59104163.md`
