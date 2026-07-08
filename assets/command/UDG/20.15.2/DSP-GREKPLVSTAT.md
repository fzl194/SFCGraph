---
id: UDG@20.15.2@MMLCommand@DSP GREKPLVSTAT
type: MMLCommand
name: DSP GREKPLVSTAT（查询GRE隧道KeepAlive报文计数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: GREKPLVSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- GRE管理
- GRE隧道KeepAlive报文计数
status: active
---

# DSP GREKPLVSTAT（查询GRE隧道KeepAlive报文计数）

## 功能

该命令用于显示GRE隧道的Keepalive报文计数。

使用GRE隧道的Keepalive功能，在业务模块选择承载隧道时，可防止选择对端不可达的GRE隧道，避免造成数据丢失。为了获取隧道Keepalive的状态，可使用该命令显示Keepalive报文计数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLNAME | 隧道名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GRE隧道接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：字符串形式为Tunnel+接口编号。 接口编号为一维或三维（格式为X/Y/Z）。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GREKPLVSTAT]] · GRE隧道KeepAlive报文计数（GREKPLVSTAT）

## 使用实例

显示设备上的Tunnel1的Keepalive报文计数：

```
DSP GREKPLVSTAT:TNLNAME="Tunnel1";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                 隧道名称  =  Tunnel1
    发送Keepalive报文个数  =  0
接收Keepalive报文应答个数  =  0
    接收Keepalive报文个数  =  0
发送Keepalive报文应答个数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-GREKPLVSTAT.md`
