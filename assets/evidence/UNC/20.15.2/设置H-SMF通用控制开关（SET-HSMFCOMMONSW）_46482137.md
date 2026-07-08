# 设置H-SMF通用控制开关（SET HSMFCOMMONSW）

- [命令功能](#ZH-CN_MMLREF_0000001946482137__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001946482137__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001946482137__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001946482137__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001946482137)

**适用NF：SMF**

该命令用于设置H-SMF通用控制开关。

## [注意事项](#ZH-CN_MMLREF_0000001946482137)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SERVINGNODEIPSW |
| --- |
| DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001946482137)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001946482137)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVINGNODEIPSW | 服务节点IP地址开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制SEPP组网场景下，N40接口消息是否不携带服务节点IP地址。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：<br>当该参数值为ENABLE时，SEPP组网场景下，N40接口消息不携带服务节点IP地址；<br>当该参数值为DISABLE时，N40接口消息携带服务节点IP地址为SEPP地址；<br>该参数仅在servingNode改变后立即生效。 |

## [使用实例](#ZH-CN_MMLREF_0000001946482137)

设置H-SMF通用控制开关：

```
SET HSMFCOMMONSW: SERVINGNODEIPSW=ENABLE;
```
