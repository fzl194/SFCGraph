---
id: UDG@20.15.2@MMLCommand@DSP HTTPLNK
type: MMLCommand
name: DSP HTTPLNK（显示HTTP链路信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: HTTPLNK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP链路管理
status: active
---

# DSP HTTPLNK（显示HTTP链路信息）

## 功能

该命令用于显示HTTP服务端链路信息，包括HTTP服务端链路的源目的IP地址和源目的端口号，以及该链路所在的POD名称和关联的资源ID等。可用于查询HTTP服务端链路的分布情况，协助定位HTTP服务端链路分布相关问题。

> **说明**
> 推荐使用IP地址作为筛选条件查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP服务端链路所在的POD名称。该POD名称可通过<br>[**DSP HTTPPROCESS**](../HTTP进程状态管理/显示HTTP进程信息（DSP HTTPPROCESS）_29053327.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置的地址的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4地址）”：IPv4地址<br>- “IPv6（IPv6地址）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| DSTIPV4 | 目的IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于显示HTTP服务端链路的目的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIPV6 | 目的IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于显示HTTP服务端链路的目的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPLNK]] · HTTP链路信息（HTTPLNK）

## 使用实例

若运营商想要查询HTTP服务端链路信息，可使用如下命令：

```
%%DSP HTTPLNK:;%%
RETCODE = 0  操作成功

结果如下
------------------------
POD名称                  资源ID  源IPv4地址   源IPv6地址    源端口号      目的IPv4地址    目的IPv6地址     目的端口号   

sbim-pod-569ffb9dc5-nrgl6  127    172.16.0.1         ::    5001         172.16.0.2         ::            31105    
sbim-pod-569ffb9dc5-nrgl6  127    172.16.0.3         ::    5001         172.16.0.4         ::            31105    
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-HTTPLNK.md`
