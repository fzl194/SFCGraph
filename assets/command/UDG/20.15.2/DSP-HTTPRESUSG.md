---
id: UDG@20.15.2@MMLCommand@DSP HTTPRESUSG
type: MMLCommand
name: DSP HTTPRESUSG（显示HTTP资源使用信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: HTTPRESUSG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP资源流控管理
status: active
---

# DSP HTTPRESUSG（显示HTTP资源使用信息）

## 功能

该命令用于显示HTTP资源使用信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询资源使用信息的类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYPEERIP（对端IP）”：对端IP<br>- “BYPOD（POD名称）”：POD名称<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"BYPOD"时为条件必选参数。<br>参数含义：该参数用于指定HTTP资源所在的POD名称。该POD名称可通过<br>[**DSP HTTPPROCESS**](../../HTTP管理/HTTP进程状态管理/显示HTTP进程信息（DSP HTTPPROCESS）_29053327.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PID | PID | 可选必选说明：该参数在"QUERYTYPE"配置为"BYPOD"时为条件必选参数。<br>参数含义：该参数用于指定查询的进程标识。该进程标识可通过<br>[**DSP HTTPPROCESS**](../../HTTP管理/HTTP进程状态管理/显示HTTP进程信息（DSP HTTPPROCESS）_29053327.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| PEERIPTYPE | 对端IP地址类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"BYPEERIP"时为条件必选参数。<br>参数含义：该参数用于指定查询对端IP地址的类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4地址）”：IPv4地址<br>- “IPv6（IPv6地址）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"PEERIPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPRESUSG]] · HTTP资源使用信息（HTTPRESUSG）

## 使用实例

- 指定POD查询资源使用信息，可以执行下面的命令：
  ```
  %%DSP HTTPRESUSG: QUERYTYPE=BYPOD, PODNAME="vusn-pod-0", PID=17;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  资源类型       POD名称    PID  对端IP地址类型        对端IPV4地址      对端IPV6地址      本端实体类型        资源门限       令牌使用率(%)   令牌总数        空闲态令牌数量  占用态令牌数量  共享令牌数量

  REQCB          vusn-pod-0  17   IPv4 Address          192.168.1.1       ::                 Client              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  17   IPv4 Address          192.168.1.1       ::                 Server              100             0               0                0               0               32640     
  (结果个数 = 2)
  ```
- 指定IP地址查询资源使用信息，可以执行下面的命令：
  ```
  %%DSP HTTPRESUSG: QUERYTYPE=BYPEERIP, PEERIPTYPE=IPv4, PEERIPV4="192.168.1.1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  资源类型       POD名称    PID  对端IP地址类型        对端IPV4地址      对端IPV6地址      本端实体类型        资源门限       令牌使用率(%)   令牌总数        空闲态令牌数量  占用态令牌数量  共享令牌数量

  REQCB          vusn-pod-0  17   IPv4 Address          192.168.1.1        ::                 Client              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  17   IPv4 Address          192.168.1.1        ::                 Server              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  20   IPv4 Address          192.168.1.1        ::                 Client              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  20   IPv4 Address          192.168.1.1        ::                 Server              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  18   IPv4 Address          192.168.1.1        ::                 Client              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  18   IPv4 Address          192.168.1.1        ::                 Server              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  19   IPv4 Address          192.168.1.1        ::                 Client              100             0               0                0               0               32640     
  REQCB          vusn-pod-0  19   IPv4 Address          192.168.1.1        ::                 Server              100             0               0                0               0               32640     
  (结果个数 = 8)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-HTTPRESUSG.md`
