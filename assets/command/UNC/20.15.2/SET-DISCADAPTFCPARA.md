---
id: UNC@20.15.2@MMLCommand@SET DISCADAPTFCPARA
type: MMLCommand
name: SET DISCADAPTFCPARA（设置服务发现自适应流控全局配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DISCADAPTFCPARA
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 服务发现自适应流控
status: active
---

# SET DISCADAPTFCPARA（设置服务发现自适应流控全局配置）

## 功能

![](设置服务发现自适应流控全局配置（SET DISCADAPTFCPARA）_10690450.assets/notice_3.0-zh-cn_2.png)

如果CODES被设置为非流控返回码，可能会发生误流控导致服务发现速率被限制。

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于设置服务发现自适应流控全局配置。系统会根据这些配置和当前状态来判断是否要进行流控。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CODES |
| --- |
| 429-503-504-604-605 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CODES | 自适应流控NRF返回码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自适应流控NRF返回码。如果服务发现的NRF返回码匹配这里的配置，则认为本次服务发现处于流控状态；系统会根据这些返回码的统计信息动态调整到NRF服务发现的速率。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~1024。只允许输入数字和"-"，"-"用于分隔不同的返回码。默认值：429-503-504-604-605，正则表达式："[0-9]{1,3}(-[0-9]{1,3})*"。<br>默认值：无。<br>配置原则：<br>根据这些返回码判断是否要自适应流控。<br>考虑到不同厂家NRF的实现可能有差异，需要支持配置返回码列表。 |

## 操作的配置对象

- [服务发现自适应流控全局配置（DISCADAPTFCPARA）](configobject/UNC/20.15.2/DISCADAPTFCPARA.md)

## 使用实例

设置NRF流控返回码为429、503和604

```
%%SET DISCADAPTFCPARA: CODES="429-503-604", CONFIRM=Y;%%
RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置服务发现自适应流控全局配置（SET-DISCADAPTFCPARA）_10690450.md`
