---
id: UNC@20.15.2@MMLCommand@LST NDIFRAROUTE
type: MMLCommand
name: LST NDIFRAROUTE（查询接口上ND RA路由配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NDIFRAROUTE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND RA路由信息
status: active
---

# LST NDIFRAROUTE（查询接口上ND RA路由配置信息）

## 功能

该命令用于接口上ND RA路由配置信息查询。

若不指定IFNAME参数时，则显示所有接口的RA路由配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NDIFRAROUTE]] · 接口上ND RA路由配置信息（NDIFRAROUTE）

## 使用实例

查询接口上ND RA路由配置信息：

```
LST NDIFRAROUTE:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
           接口名  =  Ethernet64/0/4
     IPv6地址前缀  =  2001:db8::
         前缀长度  =  70
路由存活时间（s）  =  888
     路由器优先级  =  低
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NDIFRAROUTE.md`
