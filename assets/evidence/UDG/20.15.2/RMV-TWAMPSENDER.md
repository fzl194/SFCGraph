# 删除TWAMP发送端（RMV TWAMPSENDER）

- [命令功能](#ZH-CN_MMLREF_0000001127262292__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001127262292__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001127262292__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001127262292__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001127262292)

该命令用于删除TWAMP发送端。

> **说明**
> 该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001127262292)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001127262292)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTID | 客户端ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置客户端ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~12000。<br>默认值：无<br>配置原则：<br>CLIENTID必须在<br>[**ADD TWAMPCLIENT**](../TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>已经配置，可以用<br>[**LST TWAMPCLIENT**](../TWAMP客户端配置/查询TWAMP客户端（LST TWAMPCLIENT）_27262286.md)<br>查询。 |

## [使用实例](#ZH-CN_MMLREF_0000001127262292)

删除客户端ID为1的发送端实例：

```
RMV TWAMPSENDER: CLIENTID=1;
```
